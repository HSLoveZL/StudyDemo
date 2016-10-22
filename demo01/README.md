**_The frame of ShotPlaneGame:_**

    1.加载背景音乐
    2.播放背景音乐（设置为单曲循环）
    3.我方飞机生成
    interval = 0

    进入死循环：
        while True：
            if 用户关闭了窗口:
                关闭程序

            interval += 1
            if interval = 50:
                interval = 0
                小飞机诞生
            小飞机移动一个位置
            屏幕刷新

            if 用户鼠标位置移动:
                我方飞机中心位置为用户鼠标位置
                屏幕刷新

            if 我方飞机与小飞机发生撞机事件:
                我方挂，播放背景音乐
                修改我方飞机图案
                打印“GameOver”
                停止背景音乐，最好淡出停止

