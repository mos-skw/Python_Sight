import matplotlib.pyplot as plt
import numpy as np


# 方案A：使用英文标签（推荐，最简单）
def create_sales_chart_english():
    """使用英文标签创建销售趋势图"""
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [2000, 2500, 3000, 3500, 4000, 4500,
             5000, 5500, 6000, 6500, 7000, 7500]

    plt.figure(figsize=(12, 6))

    # 绘制折线图
    plt.plot(months, sales, marker='o', linewidth=2, markersize=8,
             color='#FF6B6B', markerfacecolor='#4ECDC4',
             markeredgecolor='#45B7D1', markeredgewidth=2)

    # 添加数据标签
    for i, (month, sale) in enumerate(zip(months, sales)):
        plt.text(i, sale + 100, f'{sale}', ha='center', va='bottom', fontsize=10)

    # 标题和标签（使用英文）
    plt.title('Monthly Sales Trend 2024', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Month', fontsize=12, labelpad=10)
    plt.ylabel('Sales (RMB)', fontsize=12, labelpad=10)

    # 网格和背景
    plt.ylim(1500, 8000)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.gca().set_facecolor('#F8F9FA')

    # 平均线
    avg_sales = np.mean(sales)
    plt.axhline(y=avg_sales, color='#95A5A6', linestyle='--', alpha=0.8,
                label=f'Average: {avg_sales:.0f} RMB')

    plt.legend()
    plt.tight_layout()
    plt.show()

    # 保存
    plt.savefig('sales_trend.png', dpi=300, bbox_inches='tight')
    print("图表已保存为 'sales_trend.png'")


# 运行
create_sales_chart_english()