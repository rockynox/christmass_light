ANIMATIONS = [
    [{
        "name": "Fireplace",
        "is_celebration": False,
        "max_duration": 50000,
        "max_speed": 300,
        "full_blink": False,
        "weighted_colors": [
            [(150, 50, 00, 0), 50],  # Yellow
            [(150, 60, 00, 0), 50],  # Yellow
            [(150, 70, 00, 0), 50],  # Yellow
            [(100, 30, 0, 5), 20],
            [(50, 20, 0, 0), 10],
            [(170, 10, 0, 0), 10],  # Red warm
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
    }, 3]
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
