import clips

env = clips.Environment()

class_string = """
(defclass MyClass (is-a USER)
  (slot One)
  (slot Two))
"""
handler_string = """
(defmessage-handler MyClass handler ()
  (+ ?self:One ?self:Two))
"""
env.build(class_string)
env.build(handler_string)

instance = env.make_instance('(instance-name of MyClass (One 1) (Two 2))')
assert instance['One'] == 1
assert instance['Two'] == 2
instance.send('handler')