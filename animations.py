ANIMATIONS = [
    [{
        "name": "Fireplace",
        "is_celebration": False,
        "max_duration": 500000,
        "max_speed": 500,
        "full_blink": False,
        "weighted_colors": [
            [(100, 25, 00, 0), 50],  # Yellow
            [(150, 10, 0, 0), 40],  # Red
            [(170, 10, 0, 0), 20],  # Red warm
            [(255, 186, 38, 200), 2],  # Gold
        ]
    }, 10],
    [{
        "name": "TV",
        "is_celebration": False,
        "max_duration": 2000,
        "max_speed": 300,
        "full_blink": True,
        "weighted_colors": [
            [(43, 134, 17, 0), 10],
            [(43, 134, 230, 0), 10],
            [(60, 60, 117, 0), 1],
        ]
    }, 2]
]

CELEBRATIONS = [
    [{
        "name": "Celebration 1",
        "is_celebration": True,
        "max_duration": 100000,
        "max_speed": 30,
        "full_blink": True,
        "weighted_colors": [
            [(0, 0, 0, 0), 10],  # Black
            [(0, 0, 70, 200), 30],  # White
            [(255, 22, 0, 0), 20],  # Red
            [(75, 188, 23, 0), 20],
        ]
    }, 1]
]
