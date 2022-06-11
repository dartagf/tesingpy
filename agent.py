
# reprensentasi dari sebuah object.
class agent:
    def __init__(self, name, damage, meta, weapon):
      self.name = name
      self.damage = damage
      self.meta = meta
      self.best_weapon = weapon

    def get_name(self):
        return f"hi, my name is {self.name}, "

    def get_damage(self):
        return f"my damge is {self.damage}, "
    
    def get_meta(self):
        return f"i"m {self.meta} now, "

    def get_weapon(self):
        return f"my best weapon {self.best_weapon}"

    def get_all_data(self):
        return f"{self.get_name()} {get_damage()} {get_weapon()}"