class pet():

    def __init__(self,name,type,color,height,sound,owner):
        self.name = name
        self.type = type
        self.color = color
        self.height = height
        self.sound = sound
        self.owner = owner
        print('Object has been create')

    def set_type(self,type):

        if type == cat:
            return cat() and print('cats are the best pet')

        else:
            return 'Good for you'

    def __repr__(self):

        return '{} is a {} {} ,around {}cm height.sounds like {} ,owned by{}'.format(self.name,
                                                                                     self.color,
                                                                                     self.type,
                                                                                     self.height,
                                                                                     self.sound,
                                                                                     self.owner)
    def __del__(self):
        return 'Object has been deleted'

class cat(pet):

    def __init__(self,name,type,color,height,sound,owner,skill):

        super().__init__(name,type,color,height,sound,owner)
        self.skill =skill

    def __repr__(self):

        return '{} is a {} {} ,has a skill of {}'.format(self.name,
                                                         self.color,
                                                         self.type,
                                                         self.skill)
mia = cat('mia','cat','black',25,'enen','frank and carrie','catch')

print(mia.__repr__())
