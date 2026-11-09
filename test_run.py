import os
import time
from dotenv import load_dotenv
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 1. 加载 .env (现在只需要 DeepSeek 的 Key 了)
load_dotenv()

# 2. 从官方默认配置起步
config = DEFAULT_CONFIG.copy()

# 3. 覆盖配置：全面拥抱 yfinance，彻底抛弃 finnhub
config.update({
    "llm_provider": "deepseek",
    "deep_think_llm": "deepseek-chat",
    "quick_think_llm": "deepseek-chat",
    "backend_url": "https://api.deepseek.com",
    "data_cache_dir": "./cache",
    "results_dir": "./results",
    "logs_dir": "./logs",
    "max_debate_rounds": 2,
    "max_risk_discuss_rounds": 1,
    "online_tools": True,
    "data_vendors": {
        "core_stock_apis": "yfinance",
        "technical_indicators": "yfinance",
        "fundamental_data": "yfinance",
        "news_data": "yfinance"
    }
})

def main():
    print("正在初始化 TradingAgents...")
    ta = TradingAgentsGraph(debug=True, config=config)

    ticker = "GOOGL"
    date = "2026-11-09"

    print(f"\n开始分析 {ticker} 在 {date} 的表现，请稍等（大约需要 1-2 分钟）...\n")
    
    start_time = time.time()
    
    try:
        # 运行多智能体图
        state, decision = ta.propagate(ticker, date)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print("\n" + "="*50)
        print(f"分析完成！耗时: {elapsed_time:.2f} 秒")
        print(f"最终决策 (Final Decision): {decision}")
        print("="*50)
        
    except Exception as e:
        print(f"\n运行报错了: {e}")

if __name__ == "__main__":
    main()