import clips

env = clips.Environment()

env.load('test.clp')
env.assert_string('(jumlahsudut 3)')
env.assert_string('(jumlahsudutsama 2)')
env.assert_string('(jumlahsudutsiku 1)')


# print(env.eval('(assert (ayah "z"))'))
env.eval('(run)')


    
# print(env.run())

for fact in env.facts():
    print(str(fact) == "(samakaki)")



# for activation in env.activations():
#     print(activation.name)