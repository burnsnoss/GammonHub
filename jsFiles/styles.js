import React, {StyleSheet, Dimensions, PixelRatio} from "react-native";
const {width, height, scale} = Dimensions.get("window"),
    vw = width / 100,
    vh = height / 100,
    vmin = Math.min(vw, vh),
    vmax = Math.max(vw, vh);

export default StyleSheet.create({
    "body": {
        "marginTop": 0,
        "marginRight": "auto",
        "marginBottom": 0,
        "marginLeft": "auto"
    },
    "page": {
        "height": 666,
        "minHeight": "100%",
        "width": "100%",
        "zIndex": 2,
        "position": "absolute"
    },
    "yt": {
        "position": "absolute",
        "zIndex": 1
    }
});