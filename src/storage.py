"""
数据存储模块
支持CSV存储和JSON每日报告
"""
import csv
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATA_DIR, CSV_FILE, DAILY_DIR


class NewsStorage:
    """新闻存储管理器"""
    
    def __init__(self):
        self._ensure_dirs()
        self._ensure_csv()
    
    def _ensure_dirs(self):
        """确保目录存在"""
        os.makedirs(DATA_DIR, exist_ok=True)
        os.makedirs(DAILY_DIR, exist_ok=True)
    
    def _ensure_csv(self):
        """确保CSV文件存在并有表头"""
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'date',           # 日期
                    'category',       # 分类（国内/国际）
                    'index',          # 序号
                    'title',          # 标题
                    'summary',        # 摘要
                    'importance',     # 重要性
                    'impact_score',   # 影响力评分
                    'reason',         # 入选理由
                    'source',         # 来源
                    'url',            # 链接
                    'tags',           # 标签
                    'created_at'      # 记录创建时间
                ])
    
    def save_daily_report(self, processed_data: Dict[str, Any]) -> str:
        """保存每日报告为JSON"""
        date = processed_data.get("date", datetime.now().strftime("%Y-%m-%d"))
        filename = f"{date}.json"
        filepath = os.path.join(DAILY_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 每日报告已保存: {filepath}")
        return filepath
    
    def append_to_csv(self, processed_data: Dict[str, Any]) -> int:
        """追加数据到CSV"""
        date = processed_data.get("date", datetime.now().strftime("%Y-%m-%d"))
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        rows_added = 0
        
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # 写入国内动态
            for news in processed_data.get("domestic", []):
                writer.writerow([
                    date,
                    "国内",
                    news.get("index", ""),
                    news.get("title", ""),
                    news.get("summary", ""),
                    news.get("importance", ""),
                    news.get("impact_score", ""),
                    news.get("reason", ""),
                    news.get("source", ""),
                    news.get("url", ""),
                    ",".join(news.get("tags", [])),
                    created_at
                ])
                rows_added += 1
            
            # 写入国际动态
            for news in processed_data.get("international", []):
                writer.writerow([
                    date,
                    "国际",
                    news.get("index", ""),
                    news.get("title", ""),
                    news.get("summary", ""),
                    news.get("importance", ""),
                    news.get("impact_score", ""),
                    news.get("reason", ""),
                    news.get("source", ""),
                    news.get("url", ""),
                    ",".join(news.get("tags", [])),
                    created_at
                ])
                rows_added += 1
        
        print(f"✓ 已添加 {rows_added} 条记录到CSV")
        return rows_added
    
    def get_daily_report(self, date: str) -> Dict[str, Any]:
        """获取指定日期的报告"""
        filepath = os.path.join(DAILY_DIR, f"{date}.json")
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return None
    
    def get_all_dates(self) -> List[str]:
        """获取所有有报告的日期"""
        dates = []
        
        if os.path.exists(DAILY_DIR):
            for filename in os.listdir(DAILY_DIR):
                if filename.endswith('.json'):
                    date = filename.replace('.json', '')
                    dates.append(date)
        
        return sorted(dates, reverse=True)
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计数据"""
        stats = {
            "total_days": 0,
            "total_domestic": 0,
            "total_international": 0,
            "by_date": [],
            "by_importance": {"高": 0, "中": 0, "低": 0}
        }
        
        if not os.path.exists(CSV_FILE):
            return stats
        
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            date_counts = {}
            
            for row in reader:
                date = row.get('date', '')
                category = row.get('category', '')
                importance = row.get('importance', '')
                
                # 按日期统计
                if date not in date_counts:
                    date_counts[date] = {"domestic": 0, "international": 0}
                
                if category == "国内":
                    date_counts[date]["domestic"] += 1
                    stats["total_domestic"] += 1
                elif category == "国际":
                    date_counts[date]["international"] += 1
                    stats["total_international"] += 1
                
                # 按重要性统计
                if importance in stats["by_importance"]:
                    stats["by_importance"][importance] += 1
        
        stats["total_days"] = len(date_counts)
        stats["by_date"] = [
            {"date": d, **counts} 
            for d, counts in sorted(date_counts.items(), reverse=True)
        ]
        
        return stats
    
    def generate_index_json(self) -> str:
        """生成索引JSON文件供前端使用"""
        dates = self.get_all_dates()
        stats = self.get_statistics()
        
        index_data = {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dates": dates,
            "statistics": stats
        }
        
        index_path = os.path.join(DATA_DIR, "index.json")
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 索引文件已更新: {index_path}")
        return index_path


def save_news(processed_data: Dict[str, Any]) -> None:
    """保存新闻的主函数"""
    storage = NewsStorage()
    storage.save_daily_report(processed_data)
    storage.append_to_csv(processed_data)
    storage.generate_index_json()


if __name__ == "__main__":
    # 测试存储
    test_data = {
        "date": "2024-12-09",
        "generated_at": "2024-12-09 16:00:00",
        "domestic": [
            {
                "index": 1,
                "title": "测试新闻",
                "summary": "这是测试摘要",
                "importance": "高",
                "source": "测试来源",
                "url": "https://example.com",
                "tags": ["AI", "测试"]
            }
        ],
        "international": [],
        "summary": "测试总结"
    }
    
    save_news(test_data)
