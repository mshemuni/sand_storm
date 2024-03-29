from sand_storm import Window, World


def main():
    world = World(
        (100, 100),
        [],
        friction=6
    )

    window = Window(world, shape=(600, 600), tick=120)
    window.start()


if __name__ == '__main__':
    main()
