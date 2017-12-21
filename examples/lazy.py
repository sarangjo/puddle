from puddle import Session, Architecture

arch = Architecture.from_file('tests/arches/arch01.yaml')

with Session(arch) as session:

    a = session.input_droplet(info = 'a', location = (1,1))
    b = session.input_droplet(info = 'b', location = (3,1))
    c = session.input_droplet(info = 'c', location = (4,3))

    ab = session.mix(a, b)
    ab1, ab2 = session.split(ab)
    abc = session.mix(ab1, c)
    ababc = session.mix(abc, ab2)

    # Simple REPL setup for seeing laziness... in action?
    #
    # Run with visualization, check the auto rendering box.
    # No animation will play at first because none of the commands
    # above force evaluation.
    #
    # Force evaluation with one of the commands below:
    #
    #   Example1: "move(ababc, (2, 2))"
    #   Example2: "f = split_now(ababc)" (try it!)
    #
    # You may have to flicker the auto render check box
    # after doing so to see anything.
    #
    # CTRL-D to exit the REPL.


    #
    # These commands force evaluation of...
    #

    # ...all queued commands.
    def input(a, b):
        return session.input((a, b))

    # ...all queued commands.
    def move(a, location):
        return session.move(a, location)

    # ... all queued commands.
    def flush():
        session.flush()

    # ...commands that a and b depend on.
    def mix_now(a, b):
        return session.split_now(a,b)

    # ...commands that a depends on.
    def split_now(a):
        return session.split_now(a)

    #
    # These commands do not force evaluation.
    #

    def mix(a, b):
        return session.mix(a,b)

    def split(a):
        return session.split(a)


    import code
    code.InteractiveConsole(locals=globals()).interact()