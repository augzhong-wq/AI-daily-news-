/**
 * AI Daily News Dashboard - JavaScript Application
 * 可视化数据看板前端逻辑
 */

// 配置
const CONFIG = {
    dataPath: '../data',
    indexFile: 'index.json',
    dailyPath: 'daily'
};

// 全局状态
let state = {
    currentDate: null,
    dates: [],
    statistics: null,
    trendChart: null,
    importanceChart: null
};

// 初始化应用
document.addEventListener('DOMContentLoaded', async () => {
    console.log('🚀 AI Daily News Dashboard 初始化...');
    
    try {
        await loadIndex();
        initEventListeners();
        
        if (state.dates.length > 0) {
            await loadDailyNews(state.dates[0]);
        } else {
            showEmptyState();
        }
        
        initCharts();
        updateStatistics();
        
    } catch (error) {
        console.error('初始化失败:', error);
        showError('加载数据失败，请刷新页面重试');
    }
});

// 加载索引文件
async function loadIndex() {
    try {
        const response = await fetch(`${CONFIG.dataPath}/${CONFIG.indexFile}`);
        if (!response.ok) throw new Error('索引文件不存在');
        
        const data = await response.json();
        state.dates = data.dates || [];
        state.statistics = data.statistics || {};
        
        // 更新最后更新时间
        document.getElementById('last-updated').textContent = 
            `最后更新：${data.last_updated || '未知'}`;
        
        // 填充日期选择器
        populateDateSelector();
        
        console.log('✅ 索引加载成功，共有', state.dates.length, '天数据');
        
    } catch (error) {
        console.warn('索引加载失败，尝试使用演示数据:', error);
        loadDemoData();
    }
}

// 填充日期选择器
function populateDateSelector() {
    const selector = document.getElementById('date-select');
    selector.innerHTML = '';
    
    state.dates.forEach(date => {
        const option = document.createElement('option');
        option.value = date;
        option.textContent = formatDate(date);
        selector.appendChild(option);
    });
    
    if (state.dates.length > 0) {
        selector.value = state.dates[0];
        state.currentDate = state.dates[0];
    }
}

// 加载每日新闻
async function loadDailyNews(date) {
    if (!date) return;
    
    state.currentDate = date;
    document.getElementById('date-select').value = date;
    
    // 显示加载状态
    document.getElementById('domestic-news').innerHTML = '<div class="loading">加载中...</div>';
    document.getElementById('international-news').innerHTML = '<div class="loading">加载中...</div>';
    
    try {
        const response = await fetch(`${CONFIG.dataPath}/${CONFIG.dailyPath}/${date}.json`);
        if (!response.ok) throw new Error('数据文件不存在');
        
        const data = await response.json();
        
        renderNews('domestic-news', data.domestic || [], '国内');
        renderNews('international-news', data.international || [], '国际');
        
        // 更新摘要
        document.getElementById('daily-summary').textContent = 
            data.summary || '暂无摘要';
        
        console.log('✅ 加载', date, '的新闻成功');
        
    } catch (error) {
        console.error('加载每日新闻失败:', error);
        showEmptyState();
    }
}

// 渲染新闻列表
function renderNews(containerId, newsList, category) {
    const container = document.getElementById(containerId);
    
    if (!newsList || newsList.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <div class="icon">📭</div>
                <p>暂无${category}动态</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = newsList.map(news => {
        const importanceClass = getImportanceClass(news.importance);
        const importanceText = news.importance || '中';
        const tags = (news.tags || []).map(tag => `<span class="tag">${tag}</span>`).join('');
        
        return `
            <div class="news-item ${importanceClass}">
                <div class="news-header">
                    <span class="news-index">${news.index}</span>
                    <h4 class="news-title">${escapeHtml(news.title || '')}</h4>
                    <span class="importance-badge ${importanceClass}">${importanceText}</span>
                </div>
                <p class="news-summary">${escapeHtml(news.summary || '')}</p>
                <div class="news-meta">
                    <span>📰 ${escapeHtml(news.source || 'N/A')}</span>
                    ${news.url ? `<a href="${news.url}" target="_blank">🔗 查看原文</a>` : ''}
                </div>
                ${tags ? `<div class="news-tags">${tags}</div>` : ''}
            </div>
        `;
    }).join('');
}

// 获取重要性样式类
function getImportanceClass(importance) {
    switch (importance) {
        case '高': return 'high';
        case '中': return 'medium';
        case '低': return 'low';
        default: return 'medium';
    }
}

// 初始化图表
function initCharts() {
    initTrendChart();
    initImportanceChart();
}

// 初始化趋势图
function initTrendChart() {
    const ctx = document.getElementById('trend-chart');
    if (!ctx) return;
    
    const byDate = state.statistics?.by_date || [];
    const labels = byDate.slice(0, 14).reverse().map(d => formatDateShort(d.date));
    const domesticData = byDate.slice(0, 14).reverse().map(d => d.domestic || 0);
    const internationalData = byDate.slice(0, 14).reverse().map(d => d.international || 0);
    
    if (state.trendChart) {
        state.trendChart.destroy();
    }
    
    state.trendChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels.length > 0 ? labels : ['暂无数据'],
            datasets: [
                {
                    label: '国内动态',
                    data: domesticData.length > 0 ? domesticData : [0],
                    borderColor: '#ff6b6b',
                    backgroundColor: 'rgba(255, 107, 107, 0.1)',
                    tension: 0.4,
                    fill: true
                },
                {
                    label: '国际动态',
                    data: internationalData.length > 0 ? internationalData : [0],
                    borderColor: '#5f27cd',
                    backgroundColor: 'rgba(95, 39, 205, 0.1)',
                    tension: 0.4,
                    fill: true
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#94a3b8'
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(71, 85, 105, 0.3)'
                    },
                    ticks: {
                        color: '#94a3b8'
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(71, 85, 105, 0.3)'
                    },
                    ticks: {
                        color: '#94a3b8',
                        stepSize: 1
                    }
                }
            }
        }
    });
}

// 初始化重要性分布图
function initImportanceChart() {
    const ctx = document.getElementById('importance-chart');
    if (!ctx) return;
    
    const byImportance = state.statistics?.by_importance || { '高': 0, '中': 0, '低': 0 };
    
    if (state.importanceChart) {
        state.importanceChart.destroy();
    }
    
    state.importanceChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['高优先级', '中优先级', '低优先级'],
            datasets: [{
                data: [byImportance['高'] || 0, byImportance['中'] || 0, byImportance['低'] || 0],
                backgroundColor: [
                    '#ef4444',
                    '#f59e0b',
                    '#22c55e'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#94a3b8'
                    }
                }
            }
        }
    });
}

// 更新统计数据
function updateStatistics() {
    const stats = state.statistics || {};
    
    document.getElementById('stat-domestic').textContent = stats.total_domestic || 0;
    document.getElementById('stat-international').textContent = stats.total_international || 0;
    document.getElementById('stat-days').textContent = stats.total_days || 0;
    document.getElementById('stat-high').textContent = stats.by_importance?.['高'] || 0;
}

// 初始化事件监听
function initEventListeners() {
    // 日期选择
    document.getElementById('date-select').addEventListener('change', (e) => {
        loadDailyNews(e.target.value);
    });
    
    // 上一天
    document.getElementById('prev-date').addEventListener('click', () => {
        const currentIndex = state.dates.indexOf(state.currentDate);
        if (currentIndex < state.dates.length - 1) {
            loadDailyNews(state.dates[currentIndex + 1]);
        }
    });
    
    // 下一天
    document.getElementById('next-date').addEventListener('click', () => {
        const currentIndex = state.dates.indexOf(state.currentDate);
        if (currentIndex > 0) {
            loadDailyNews(state.dates[currentIndex - 1]);
        }
    });
}

// 加载演示数据
function loadDemoData() {
    const today = new Date().toISOString().split('T')[0];
    
    state.dates = [today];
    state.statistics = {
        total_days: 1,
        total_domestic: 5,
        total_international: 5,
        by_importance: { '高': 4, '中': 4, '低': 2 },
        by_date: [{ date: today, domestic: 5, international: 5 }]
    };
    
    populateDateSelector();
    
    // 演示新闻数据
    const demoNews = {
        domestic: [
            {
                index: 1,
                title: "智谱AI开源AutoGLM项目",
                summary: "12月9日消息，智谱AI宣布开源AutoGLM项目，经过32个月研发构建完整Phone Use能力框架，使AI能通过视觉理解手机界面完成点击、滑动等操作。",
                importance: "高",
                source: "智谱AI",
                tags: ["智谱AI", "开源", "AutoGLM"]
            },
            {
                index: 2,
                title: "蚂蚁集团推出灵光网页版",
                summary: "12月9日消息，蚂蚁集团正式推出全模态通用AI助手灵光网页版，延续\"30秒用自然语言生成小应用\"核心优势。",
                importance: "高",
                source: "蚂蚁集团",
                tags: ["蚂蚁集团", "灵光", "AI助手"]
            }
        ],
        international: [
            {
                index: 1,
                title: "特朗普允许英伟达向中国出售H200芯片",
                summary: "12月9日消息，美国总统特朗普宣布允许英伟达向中国出售H200人工智能芯片，但要求英伟达将25%的收益支付给美国政府。",
                importance: "高",
                source: "Reuters",
                tags: ["英伟达", "AI芯片", "政策"]
            },
            {
                index: 2,
                title: "OpenAI推出o3推理模型",
                summary: "12月9日消息，OpenAI正式发布o3系列推理模型，在复杂推理任务上表现出色，成为目前最强大的AI推理模型之一。",
                importance: "高",
                source: "OpenAI",
                tags: ["OpenAI", "o3", "推理模型"]
            }
        ],
        summary: "今日共采集到5条国内动态和5条国际动态。重点关注：智谱AI开源AutoGLM; 特朗普允许H200对华出口; OpenAI发布o3模型。"
    };
    
    renderNews('domestic-news', demoNews.domestic, '国内');
    renderNews('international-news', demoNews.international, '国际');
    document.getElementById('daily-summary').textContent = demoNews.summary;
    
    console.log('📦 已加载演示数据');
}

// 显示空状态
function showEmptyState() {
    const emptyHtml = `
        <div class="empty-state">
            <div class="icon">📭</div>
            <p>暂无数据，请等待自动更新</p>
        </div>
    `;
    
    document.getElementById('domestic-news').innerHTML = emptyHtml;
    document.getElementById('international-news').innerHTML = emptyHtml;
}

// 显示错误
function showError(message) {
    const errorHtml = `
        <div class="empty-state">
            <div class="icon">❌</div>
            <p>${message}</p>
        </div>
    `;
    
    document.getElementById('domestic-news').innerHTML = errorHtml;
    document.getElementById('international-news').innerHTML = errorHtml;
}

// 工具函数：格式化日期
function formatDate(dateStr) {
    const date = new Date(dateStr);
    const options = { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' };
    return date.toLocaleDateString('zh-CN', options);
}

function formatDateShort(dateStr) {
    const date = new Date(dateStr);
    return `${date.getMonth() + 1}/${date.getDate()}`;
}

// 工具函数：HTML转义
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
