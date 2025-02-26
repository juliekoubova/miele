"""Device capabilities."""

# API Version 1.0.5

DEV_TYPES = {
    1: "Washing Machine",
    2: "Thumble Dryer",
    7: "Dishwasher",
    19: "Fridge",
    20: "Freezer",
    74: "TwoInOne Hob",
}

STATE_CAPABILITIES = {
    19: {
        "ProgramID",
        "status",
        "programType",
        "targetTemperature",
        "temperature",
        "signalInfo",
        "signalFailure",
        "signalDoor",
        "remoteEnable",
    },
    20: {
        "ProgramID",
        "status",
        "programType",
        "targetTemperature",
        "temperature",
        "signalInfo",
        "signalFailure",
        "signalDoor",
        "remoteEnable",
    },
}

ACTION_CAPABILITIES = {
    19: {"targetTemperature", "startSupercooling"},
    20: {"targetTemperature", "startSuperfreezing"},
}

LIVE_ACTION_CAPABILITIES = {
    "711934968": {
        "processAction": [4],
        "light": [],
        "ambientLight": [],
        "startTime": [],
        "ventilationStep": [],
        "programId": [],
        "targetTemperature": [{"zone": 1, "min": -26, "max": -16}],
        "deviceName": True,
        "powerOn": False,
        "powerOff": False,
        "colors": [],
        "modes": [1],
    },
    "711944869": {
        "processAction": [6],
        "light": [],
        "ambientLight": [],
        "startTime": [],
        "ventilationStep": [],
        "programId": [],
        "targetTemperature": [{"zone": 1, "min": 1, "max": 9}],
        "deviceName": True,
        "powerOn": False,
        "powerOff": False,
        "colors": [],
        "modes": [1],
    },
}

TEST_DATA_1 = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 1,
            "value_localized": "Washing machine",
        },
        "deviceName": "",
        "protocolVersion": 4,
        "deviceIdentLabel": {
            "fabNumber": "<fabnumber01>",
            "fabIndex": "00",
            "techType": "WWI860",
            "matNumber": "",
            "swids": ["000"],
        },
        "xkmIdentLabel": {
            "techType": "EK057",
            "releaseVersion": "08.15",
        },
    },
    "state": {
        "ProgramID": {
            "value_raw": 1,
            "value_localized": "Cottons",
            "key_localized": "Program name",
        },
        "status": {
            "value_raw": 1,
            "value_localized": "Off",
            "key_localized": "status",
        },
        "programType": {
            "value_raw": 1,
            "value_localized": "Own programme",
            "key_localized": "Program type",
        },
        "programPhase": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Program phase",
        },
        "remainingTime": [0, 0],
        "startTime": [0, 0],
        "targetTemperature": [
            {"value_raw": -32766, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "temperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": True,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": None,
        "light": None,
        "elapsedTime": [0, 0],
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": 1600,
            "value_localized": "1600",
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Fan level",
        },
        "plateStep": [],
        "ecoFeedback": None,
        "batteryLevel": None,
    },
}

TEST_DATA_7 = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 7,
            "value_localized": "Dishwasher",
        },
        "deviceName": "",
        "protocolVersion": 2,
        "deviceIdentLabel": {
            "fabNumber": "<fabNumber1>",
            "fabIndex": "64",
            "techType": "G6865-W",
            "matNumber": "<matNumber1>",
            "swids": [
                "<swid1>",
                "<swid2>",
                "<swid3>",
                "<...>",
            ],
        },
        "xkmIdentLabel": {"techType": "EK039W", "releaseVersion": "02.72"},
    },
    "state": {
        "ProgramID": {
            "value_raw": 38,
            "value_localized": "QuickPowerWash",
            "key_localized": "Program name",
        },
        "status": {
            "value_raw": 5,
            "value_localized": "In use",
            "key_localized": "status",
        },
        "programType": {
            "value_raw": 2,
            "value_localized": "Automatic programme",
            "key_localized": "Program type",
        },
        "programPhase": {
            "value_raw": 1799,
            "value_localized": "Drying",
            "key_localized": "Program phase",
        },
        "remainingTime": [0, 15],
        "startTime": [0, 0],
        "targetTemperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"}
        ],
        "temperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": False,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": None,
        "light": None,
        "elapsedTime": [0, 59],
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": None,
            "value_localized": None,
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Fan level",
        },
        "plateStep": [],
        "ecoFeedback": {
            "currentWaterConsumption": {
                "unit": "l",
                "value": 12,
            },
            "currentEnergyConsumption": {
                "unit": "kWh",
                "value": 1.4,
            },
            "waterForecast": 0.2,
            "energyForecast": 0.1,
        },
        "batteryLevel": None,
    },
}

TEST_DATA_18 = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 18,
            "value_localized": "Cooker Hood",
        },
        "deviceName": "",
        "protocolVersion": 2,
        "deviceIdentLabel": {
            "fabNumber": "<fabNumber3>",
            "fabIndex": "64",
            "techType": "Fläkt",
            "matNumber": "<matNumber3>",
            "swids": [
                "<swid1>",
                "<swid2>",
                "<swid3>",
                "<...>",
            ],
        },
        "xkmIdentLabel": {"techType": "EK039W", "releaseVersion": "02.72"},
    },
    "state": {
        "ProgramID": {
            "value_raw": 1,
            "value_localized": "Off",
            "key_localized": "Program name",
        },
        "status": {
            "value_raw": 1,
            "value_localized": "Off",
            "key_localized": "status",
        },
        "programType": {
            "value_raw": 0,
            "value_localized": "Program",
            "key_localized": "Program type",
        },
        "programPhase": {
            "value_raw": 4608,
            "value_localized": "",
            "key_localized": "Program phase",
        },
        "remainingTime": [0, 0],
        "startTime": [0, 0],
        "targetTemperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"}
        ],
        "temperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": False,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": 2,
        "light": 2,
        "elapsedTime": {},
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": None,
            "value_localized": None,
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": 0,
            "value_localized": "0",
            "key_localized": "Fan level",
        },
        "plateStep": [],
        "ecoFeedback": None,
        "batteryLevel": None,
    },
}

TEST_DATA_21 = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 21,
            "value_localized": "Fridge freezer",
        },
        "deviceName": "",
        "protocolVersion": 203,
        "deviceIdentLabel": {
            "fabNumber": "**REDACTED**",
            "fabIndex": "00",
            "techType": "KFN 7734 D",
            "matNumber": "11642200",
            "swids": ["000"],
        },
        "xkmIdentLabel": {
            "techType": "EK037LHBM",
            "releaseVersion": "32.15",
        },
    },
    "state": {
        "ProgramID": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Program name",
        },
        "status": {
            "value_raw": 5,
            "value_localized": "In use",
            "key_localized": "status",
        },
        "programType": {
            "value_raw": 0,
            "value_localized": "Program",
            "key_localized": "Program type",
        },
        "programPhase": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Program phase",
        },
        "remainingTime": [0, 0],
        "startTime": [0, 0],
        "targetTemperature": [
            {"value_raw": 500, "value_localized": 5.0, "unit": "Celsius"},
            {"value_raw": -1800, "value_localized": -18.0, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "temperature": [
            {"value_raw": 493, "value_localized": 4.93, "unit": "Celsius"},
            {"value_raw": -1807, "value_localized": -18.07, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": False,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": None,
        "light": None,
        "elapsedTime": [],
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Fan level",
        },
        "plateStep": [],
        "ecoFeedback": None,
        "batteryLevel": None,
    },
}

TEST_DATA_23 = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 23,
            "value_localized": "Robot vacuum cleaner",
        },
        "deviceName": "Batman",
        "protocolVersion": 0,
        "deviceIdentLabel": {
            "fabNumber": "161173909",
            "fabIndex": "32",
            "techType": "RX3",
            "matNumber": "11686510",
            "swids": [
                "<swid1>",
                "<swid2>",
                "<swid3>",
                "<...>",
            ],
        },
        "xkmIdentLabel": {"techType": "", "releaseVersion": ""},
    },
    "state": {
        "ProgramID": {
            "value_raw": 1,
            "value_localized": "Auto",
            "key_localized": "Program name",
        },
        "status": {"value_raw": 2, "value_localized": "On", "key_localized": "status"},
        "programType": {
            "value_raw": 0,
            "value_localized": "Program",
            "key_localized": "Program type",
        },
        "programPhase": {
            "xvalue_raw": 5889,
            "zvalue_raw": 5904,
            "value_raw": 5893,
            "value_localized": "in the base station",
            "key_localized": "Program phase",
        },
        "remainingTime": [0, 0],
        "startTime": [0, 0],
        "targetTemperature": [],
        "temperature": [],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": False,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": None,
        "light": None,
        "elapsedTime": [0, 0],
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": None,
            "value_localized": None,
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Fan level",
        },
        "plateStep": [],
        "ecoFeedback": None,
        "batteryLevel": 65,
    },
}

TEST_DATA_24 = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 24,
            "value_localized": "Washer dryer",
        },
        "deviceName": "",
        "protocolVersion": 4,
        "deviceIdentLabel": {
            "fabNumber": "<fabNumber2>",
            "fabIndex": "32",
            "techType": "WTR870",
            "matNumber": "<matNumber2>",
            "swids": [
                "<swid1>",
                "<swid2>",
                "<swid3>",
                "<...>",
            ],
        },
        "xkmIdentLabel": {"techType": "EK037", "releaseVersion": "03.88"},
    },
    "state": {
        "ProgramID": {
            "value_raw": 3,
            "value_localized": "Minimum iron",
            "key_localized": "Program name",
        },
        "status": {"value_raw": 1, "value_localized": "Off", "key_localized": "status"},
        "programType": {
            "value_raw": 1,
            "value_localized": "Own programme",
            "key_localized": "Program type",
        },
        "programPhase": {
            "value_raw": 256,
            "value_localized": "",
            "key_localized": "Program phase",
        },
        "remainingTime": [1, 59],
        "startTime": [0, 0],
        "targetTemperature": [
            {"value_raw": 3000, "value_localized": 30, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "temperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": True,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": None,
        "light": None,
        "elapsedTime": [0, 17],
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": 1000,
            "value_localized": "1000",
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Fan level",
        },
        "plateStep": [],
        "ecoFeedback": None,
        "batteryLevel": None,
    },
}

TEST_DATA_74 = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 74,
            "value_localized": "",
        },
        "deviceName": "",
        "protocolVersion": 203,
        "deviceIdentLabel": {
            "fabNumber": "**REDACTED**",
            "fabIndex": "00",
            "techType": "KMDA7634",
            "matNumber": "",
            "swids": ["000"],
        },
        "xkmIdentLabel": {
            "techType": "EK039W",
            "releaseVersion": "02.72",
        },
    },
    "state": {
        "ProgramID": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Program name",
        },
        "status": {
            "value_raw": 5,
            "value_localized": "In use",
            "key_localized": "status",
        },
        "programType": {
            "value_raw": 0,
            "value_localized": "Program",
            "key_localized": "Program type",
        },
        "programPhase": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Program phase",
        },
        "remainingTime": [0, 0],
        "startTime": [0, 0],
        "targetTemperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "temperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": False,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": None,
        "light": None,
        "elapsedTime": [],
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Fan level",
        },
        "plateStep": [
            {"value_raw": 0, "value_localized": 0, "key_localized": "Power level"},
            {"value_raw": 3, "value_localized": 2, "key_localized": "Power level"},
            {"value_raw": 7, "value_localized": 4, "key_localized": "Power level"},
            {"value_raw": 15, "value_localized": 8, "key_localized": "Power level"},
            {"value_raw": 117, "value_localized": 10, "key_localized": "Power level"},
        ],
        "ecoFeedback": None,
        "batteryLevel": None,
    },
}

TEST_DATA_TEMPLATE = {
    "ident": {
        "type": {
            "key_localized": "Device type",
            "value_raw": 0,
            "value_localized": "Template",
        },
        "deviceName": "",
        "protocolVersion": 203,
        "deviceIdentLabel": {
            "fabNumber": "**REDACTED**",
            "fabIndex": "00",
            "techType": "",
            "matNumber": "",
            "swids": ["000"],
        },
        "xkmIdentLabel": {
            "techType": "",
            "releaseVersion": "",
        },
    },
    "state": {
        "ProgramID": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Program name",
        },
        "status": {
            "value_raw": 5,
            "value_localized": "In use",
            "key_localized": "status",
        },
        "programType": {
            "value_raw": 0,
            "value_localized": "Program",
            "key_localized": "Program type",
        },
        "programPhase": {
            "value_raw": 0,
            "value_localized": "",
            "key_localized": "Program phase",
        },
        "remainingTime": [0, 0],
        "startTime": [0, 0],
        "targetTemperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "temperature": [
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
            {"value_raw": -32768, "value_localized": None, "unit": "Celsius"},
        ],
        "signalInfo": False,
        "signalFailure": False,
        "signalDoor": False,
        "remoteEnable": {
            "fullRemoteControl": True,
            "smartGrid": False,
            "mobileStart": False,
        },
        "ambientLight": None,
        "light": None,
        "elapsedTime": [],
        "spinningSpeed": {
            "unit": "rpm",
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Spin speed",
        },
        "dryingStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Drying level",
        },
        "ventilationStep": {
            "value_raw": None,
            "value_localized": "",
            "key_localized": "Fan level",
        },
        "plateStep": [],
        "ecoFeedback": None,
        "batteryLevel": None,
    },
}

TEST_ACTION_21 = {
    "processAction": [4, 6],
    "light": [],
    "ambientLight": [],
    "startTime": [],
    "ventilationStep": [],
    "programId": [],
    "targetTemperature": [
        {"zone": 1, "min": 1, "max": 9},
        {"zone": 2, "min": -26, "max": -16},
    ],
    "deviceName": True,
    "powerOn": False,
    "powerOff": True,
    "colors": [],
    "modes": [1],
    "programs": [],
    "id_log": [],
}

TEST_ACTION_23 = {
    "processAction": [1],
    "light": [],
    "ambientLight": [],
    "startTime": [],
    "ventilationStep": [],
    "programId": [2, 3, 4],
    "targetTemperature": [],
    "deviceName": True,
    "powerOn": True,
    "powerOff": False,
    "colors": [],
    "modes": [],
}
