import cocos

if __name__ == '__main__':
    cocos.director.director.init()
    scene = cocos.scene.Scene()
    cocos.director.director.run(scene)
