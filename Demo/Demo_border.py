from RainbowColorizer import RC

a = "Let life be beautiful like summer flowers and death like autumn leaves"
print(RC.border(a))
a = "The world has kissed my soul with its pain, asking for its return in songs"
print(RC.border(a,color1=(255,192,203),color2=(218,112,214)))
a = "Stray birds of summer come to my window to sing and fly away. \nAnd yellow leaves of autumn, which have no songs, flutter and fall there with a sign."
print(RC.border(a,4,RC.colors4))
a = """Civilizations in the universe only have the lowest level of goodwill.
Communication will definitely expose the position of civilization.
The level of competition between civilizations is comparable to that of dark battles.
Difficult to communicate between different intelligent species.
Every civilization has a long lifespan.
                                                        ——The three body problem"""
print(RC.border(a,4,RC.colors4,title='The Dark Forest Theory',color1=(255,192,203),color2=(255,153,192),color3=(245,212,217),color4=(218,112,214)))