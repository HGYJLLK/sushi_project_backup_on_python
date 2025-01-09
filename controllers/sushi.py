class Sushi:
    def __init__(self, name, image, price):
        self.name = name
        self.image = f"controllers/sushi_img/{image}"
        self.price = price


# 初始化寿司数据
SUSHI_DATA = [
    Sushi("三文鱼寿司", "salmon_sushi.jpg", 28),
    Sushi("金枪鱼寿司", "tuna_sushi.jpg", 25),
    Sushi("虾寿司", "shrimp_sushi.jpg", 26),
    Sushi("鳗鱼寿司", "eel_sushi.jpg", 32),
    Sushi("蟹肉寿司", "crab_sushi.jpg", 30),
    Sushi("玉子寿司", "egg_sushi.jpg", 18),
    Sushi("黄尾鱼寿司", "yellow_tail_sushi.jpg", 28),
    Sushi("章鱼寿司", "octopus_sushi.jpg", 24),
    Sushi("青花鱼寿司", "mackerel_sushi.jpg", 22),
    Sushi("鱿鱼寿司", "squid_sushi.jpg", 23),
    Sushi("素寿司卷", "vegetable_roll.jpg", 20),
    Sushi("加州卷", "california_roll.jpg", 25),
    Sushi("炙烤三文鱼寿司", "seared_salmon_sushi.jpg", 32),
    Sushi("龙虾寿司", "lobster_sushi.jpg", 38),
    Sushi("鲷鱼寿司", "sea_bream_sushi.jpg", 28),
    Sushi("帝王蟹寿司", "king_crab_sushi.jpg", 45),
    Sushi("火炙牛肉寿司", "beef_sushi.jpg", 35),
    Sushi("彩虹卷", "rainbow_roll.jpg", 32),
    Sushi("梅子寿司", "plum_sushi.jpg", 18),
    Sushi("天妇罗虾寿司", "tempura_shrimp_sushi.jpg", 28)
]


def get_all_sushi():
    """获取所有寿司数据"""
    return [{"name": s.name,
             "image": s.image,
             "price": s.price}
            for s in SUSHI_DATA]


def search_sushi(keyword):
    """根据名称搜索寿司
    Args:
        keyword (str): 搜索关键词
    Returns:
        list: 匹配的寿司列表
    """
    return [{"name": s.name,
             "image": s.image,
             "price": s.price}
            for s in SUSHI_DATA if keyword in s.name]
