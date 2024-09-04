def exercise1():
    print ("Exercise 1: Cube's Surface Area")
    edges = float(input("Enter length of edges: "))
    surface_area = 6 * edges**2
    print("Surface area of the cube is: {} m2".format(surface_area))


def exercise2():
    print ("Exercise 2: Five Star Retro Video Store")
    new_videos = int(input("Enter the number of the new videos: "))
    old_videos = int(input("Enter the number of the old videos: "))

    total_videos = new_videos*3 + old_videos*2
    print("Total cost of videos is: {:.2f}$ which is {} new videos and {} old videos".format(total_videos, new_videos, old_videos))



if __name__ == "__main__":
    # exercise1()
    exercise2()

