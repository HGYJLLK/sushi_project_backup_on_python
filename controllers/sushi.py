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
    Sushi("天妇罗虾寿司", "tempura_shrimp_sushi.jpg", 28),
]

SUSHI_DETAILS = {
    "三文鱼寿司": {
        "name_en": "Salmon Sushi",
        "description": "新鲜三文鱼配上醋饭，口感细腻，富含omega-3脂肪酸",
        "steps": [
            "准备寿司醋和米饭",
            "准备新鲜三文鱼片",
            "将寿司醋拌入米饭",
            "把三文鱼片盖在米饭上",
        ],
    },
    "金枪鱼寿司": {
        "name_en": "Tuna Sushi",
        "description": "精选金枪鱼生鱼片，肉质紧实，味道鲜美",
        "steps": [
            "准备寿司醋和米饭",
            "准备金枪鱼生鱼片",
            "将寿司醋拌入米饭",
            "把金枪鱼片盖在米饭上",
        ],
    },
    "虾寿司": {
        "name_en": "Shrimp Sushi",
        "description": "新鲜虾仁煮熟后搭配醋饭，口感弹牙，营养丰富",
        "steps": [
            "准备寿司醋和米饭",
            "虾仁去壳去虾线",
            "将虾仁煮熟",
            "将寿司醋拌入米饭",
            "把煮熟的虾仁放在米饭上",
        ],
    },
    "鳗鱼寿司": {
        "name_en": "Eel Sushi",
        "description": "烤制鳗鱼配以特制酱汁，香气四溢，味道浓郁",
        "steps": [
            "准备寿司醋和米饭",
            "鳗鱼切片并烤制",
            "刷上特制蒲烧酱",
            "将寿司醋拌入米饭",
            "把烤好的鳗鱼片放在米饭上",
        ],
    },
    "蟹肉寿司": {
        "name_en": "Crab Sushi",
        "description": "精选蟹肉制成，鲜甜可口，蛋白质含量丰富",
        "steps": [
            "准备寿司醋和米饭",
            "蟹肉拆解成小块",
            "将寿司醋拌入米饭",
            "把蟹肉放在米饭上",
        ],
    },
    "玉子寿司": {
        "name_en": "Egg Sushi",
        "description": "日式玉子烧配上醋饭，口感松软，适合素食者",
        "steps": [
            "准备寿司醋和米饭",
            "制作日式玉子烧",
            "将玉子烧切片",
            "将寿司醋拌入米饭",
            "把玉子烧片放在米饭上",
        ],
    },
    "黄尾鱼寿司": {
        "name_en": "Yellow Tail Sushi",
        "description": "新鲜黄尾鱼片，肉质细嫩，油脂丰富",
        "steps": [
            "准备寿司醋和米饭",
            "准备新鲜黄尾鱼片",
            "将寿司醋拌入米饭",
            "把黄尾鱼片盖在米饭上",
        ],
    },
    "章鱼寿司": {
        "name_en": "Octopus Sushi",
        "description": "煮熟的章鱼切片，口感爽滑，富含胶原蛋白",
        "steps": [
            "准备寿司醋和米饭",
            "章鱼煮熟后切片",
            "将寿司醋拌入米饭",
            "把章鱼片放在米饭上",
        ],
    },
    "青花鱼寿司": {
        "name_en": "Mackerel Sushi",
        "description": "腌制青花鱼片，味道独特，富含DHA",
        "steps": [
            "准备寿司醋和米饭",
            "青花鱼片腌制",
            "将寿司醋拌入米饭",
            "把腌制好的青花鱼片放在米饭上",
        ],
    },
    "鱿鱼寿司": {
        "name_en": "Squid Sushi",
        "description": "新鲜鱿鱼切片，口感爽脆，低脂肪高蛋白",
        "steps": [
            "准备寿司醋和米饭",
            "鱿鱼切片",
            "将寿司醋拌入米饭",
            "把鱿鱼片放在米饭上",
        ],
    },
    "素寿司卷": {
        "name_en": "Vegetable Roll",
        "description": "多种新鲜蔬菜卷制，清爽健康，适合素食者",
        "steps": [
            "准备寿司醋和米饭",
            "准备各种新鲜蔬菜",
            "将寿司醋拌入米饭",
            "把蔬菜放入并卷起",
        ],
    },
    "加州卷": {
        "name_en": "California Roll",
        "description": "蟹棒、牛油果等材料卷制，口感丰富，深受欢迎",
        "steps": [
            "准备寿司醋和米饭",
            "准备蟹棒和牛油果",
            "将寿司醋拌入米饭",
            "把材料放入并卷起",
            "外裹上鱼子",
        ],
    },
    "炙烤三文鱼寿司": {
        "name_en": "Seared Salmon Sushi",
        "description": "表面炙烤的三文鱼，香气四溢，口感层次丰富",
        "steps": [
            "准备寿司醋和米饭",
            "三文鱼片表面炙烤",
            "将寿司醋拌入米饭",
            "把炙烤好的三文鱼片放在米饭上",
        ],
    },
    "龙虾寿司": {
        "name_en": "Lobster Sushi",
        "description": "新鲜龙虾肉，鲜甜可口，高档奢华",
        "steps": [
            "准备寿司醋和米饭",
            "龙虾煮熟取肉",
            "将寿司醋拌入米饭",
            "把龙虾肉放在米饭上",
        ],
    },
    "鲷鱼寿司": {
        "name_en": "Sea Bream Sushi",
        "description": "新鲜鲷鱼片，肉质细腻，味道清甜",
        "steps": [
            "准备寿司醋和米饭",
            "准备鲷鱼生鱼片",
            "将寿司醋拌入米饭",
            "把鲷鱼片放在米饭上",
        ],
    },
    "帝王蟹寿司": {
        "name_en": "King Crab Sushi",
        "description": "精选帝王蟹肉，鲜美无比，价格昂贵",
        "steps": [
            "准备寿司醋和米饭",
            "帝王蟹腿肉处理",
            "将寿司醋拌入米饭",
            "把蟹肉放在米饭上",
        ],
    },
    "火炙牛肉寿司": {
        "name_en": "Beef Sushi",
        "description": "高级牛肉片表面炙烤，香嫩可口，创新风味",
        "steps": [
            "准备寿司醋和米饭",
            "牛肉片表面炙烤",
            "将寿司醋拌入米饭",
            "把炙烤好的牛肉片放在米饭上",
        ],
    },
    "彩虹卷": {
        "name_en": "Rainbow Roll",
        "description": "多种生鱼片装饰的卷物，色彩缤纷，口感丰富",
        "steps": [
            "准备寿司醋和米饭",
            "准备各种生鱼片",
            "制作基础卷物",
            "在外层铺上不同的生鱼片",
        ],
    },
    "梅子寿司": {
        "name_en": "Plum Sushi",
        "description": "咸酸梅子配上醋饭，开胃爽口，独特风味",
        "steps": [
            "准备寿司醋和米饭",
            "准备腌制梅子",
            "将寿司醋拌入米饭",
            "在米饭上放入梅子",
        ],
    },
    "天妇罗虾寿司": {
        "name_en": "Tempura Shrimp Sushi",
        "description": "酥脆天妇罗虾配上醋饭，热腾香脆，深受欢迎",
        "steps": [
            "准备寿司醋和米饭",
            "制作虾天妇罗",
            "将寿司醋拌入米饭",
            "把天妇罗虾放在米饭上",
        ],
    },
}

def get_all_sushi():
    """获取所有寿司数据"""
    return [{"name": s.name, "image": s.image, "price": s.price} for s in SUSHI_DATA]

def search_sushi(keyword):
    """根据名称搜索寿司
    Args:
        keyword (str): 搜索关键词
    Returns:
        list: 匹配的寿司列表
    """
    return [
        {"name": s.name, "image": s.image, "price": s.price}
        for s in SUSHI_DATA
        if keyword in s.name
    ]

def get_sushi_detail(sushi_name):
    """根据寿司名称获取详情
    Args:
        sushi_name (str): 寿司名称
    Returns:
        dict: 寿司详情数据，如果不存在返回 None
    """
    return SUSHI_DETAILS.get(sushi_name)

def add_sushi(name, image_filename, price, details):
    """添加新寿司
    Args:
        name (str): 寿司名称
        image_filename (str): 图片文件名
        price (float): 价格
        details (dict): 详情信息
    Returns:
        bool: 是否成功
    """
    # 检查是否已存在
    if any(s.name == name for s in SUSHI_DATA):
        return False, "寿司名称已存在"

    # 添加到SUSHI_DATA
    SUSHI_DATA.append(Sushi(name, image_filename, float(price)))

    # 添加到SUSHI_DETAILS
    SUSHI_DETAILS[name] = details

    return True, "添加成功"


def update_sushi(name, image_filename, price, details):
    """更新寿司信息
    Args:
        name (str): 寿司名称
        image_filename (str): 图片文件名
        price (float): 价格
        details (dict): 详情信息
    Returns:
        bool: 是否成功
    """
    # 查找索引
    index = next((i for i, s in enumerate(SUSHI_DATA) if s.name == name), -1)

    if index == -1:
        return False, "寿司不存在"

    # 更新SUSHI_DATA
    SUSHI_DATA[index] = Sushi(name, image_filename, float(price))

    # 更新SUSHI_DETAILS
    SUSHI_DETAILS[name] = details

    return True, "更新成功"


def delete_sushi(name):
    """删除寿司
    Args:
        name (str): 寿司名称
    Returns:
        bool: 是否成功
    """
    # 查找索引
    index = next((i for i, s in enumerate(SUSHI_DATA) if s.name == name), -1)

    if index == -1:
        return False, "寿司不存在"

    # 从SUSHI_DATA删除
    SUSHI_DATA.pop(index)

    # 从SUSHI_DETAILS删除
    if name in SUSHI_DETAILS:
        del SUSHI_DETAILS[name]

    return True, "删除成功"
