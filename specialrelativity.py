#I am taking a special relativity course at my school, so for this, why not model the basic equations FOR special relativity
#don't be scared about learning it either, special relativity unlike its big sister general relativity, isn't math heavy, no PDEs or ODEs, special relativity to understand it requires at most algebra level knowledge, and at an advanced level you just need to have done well in Calculus I to understand it
import matplotlib
import math
c= 3.0*10**8
def sqrt(x):
    return (x**0.5)
#it sounds stupid for me to definte a sqrt function, but for some reason whenever I just have it undefined, sqrt doesn't work for some reason and I got to define it myself, it probably should work without defining it but thats just my fix to it.
# I am taking a special relativity course at my school, so for this,
# why not model the basic equations FOR special relativity

# Special relativity unlike general relativity isn't math heavy.
# No PDEs or ODEs — mostly algebra.


c = 3.0 * 10**8  # speed of light (m/s), just know it is always constant for every observer, this is one of the main postulates of it, it is also this lack of simultaneity being why two people disagree on the same event

# These are the big big equations of special relativity, without them, special relativity and what happens when things approach the speed of light will not make sense nor will it be measurable

def gamma(v):
    # Lorentz factor, this basically tells us how time dialates or length contracts and basically is doing all of the heavy lifting for special relativity
    return 1 / sqrt(1 - (v**2 / c**2))


def t_prime(t0, v):
    # time dilation, lets assume two people have clocks, one is on earth and the other is on a spaceship at near the speed of light, lets say it takes a person on that spaceship 50 minutes to get to jupiter according to their view, however from earths view, it took them 70 minutes to get there, basically what it means is that a moving clock is much slower than one that is stationary
    return t0 * gamma(v)


def L_prime(L0, v):
    # length contraction, lets say someone from earth is watching someone in the same spaceship travelling to our nearest star(not including the sun) of Proxima centauri, that distance is about 4.24 light years and from the perspective of someone from earth that ship would take 5.3 years to get there, however from the ships perspective it would travel 2.54 light years and would make it in 3.18 years. 
    return L0 / gamma(v)


def E_total(m0, v):
    # relativistic energy, this insinuates that something that has no momentum has energy because it has mass, its alss worth to note that this comes from the full equation E^2= (pc)^2+ (m * c^2)^2, this is the full energy, E=mc^2 is just the rest energy of an object, and another way to write E is for the total energy of a particle to be gamma*mc^2, you are gonna find out in a few lines why I mentioned that
    return gamma(v) * m0 * c**2


def KE(m0, v):
    # relativistic kinetic energy, to derive for this, just remember Kinetic energy is the leftover energy that when + the rest energy becomes the total energy, so E - mc^2 =K, and E will be gamma mc^2, so you have gamma * mc^2 - mc^2 so now with basic algebra you can factor to get (gamma-1)*mc^2 and thats where Kinetic energy comes from
    return (gamma(v) - 1) * m0 * c**2


# this is the part where I ask you if you want a quick equation solver or not

print("Special Relativity Equation System")
print("Options: gamma, time dilation, length contraction, energy, kinetic energy")

choice = input("Which equation do you want to use? ").lower()

# -------------------------
# GAMMA
# -------------------------
if choice == "gamma":
    
    

    v = float(input("Enter velocity as fraction of c (0 to 1): ")) * c
    print("gamma =", gamma(v))


elif choice == "time dilation":

    v = float(input("Velocity as fraction of c (0 to 1): ")) * c
    t0 = float(input("Proper time t0 (seconds, years, etc): "))


    print("t' =", t_prime(t0, v))



elif choice == "length contraction":

    v = float(input("Velocity as fraction of c (0 to 1): ")) * c
    L0 = float(input("Proper length L0: "))

    print("L' =", L_prime(L0, v))



elif choice == "energy":

    v = float(input("Velocity as fraction of c (0 to 1): ")) * c
    m0 = float(input("Rest mass m0 (kg): "))

    print("E =", E_total(m0, v))



elif choice == "kinetic energy":

    v = float(input("Velocity as fraction of c (0 to 1): ")) * c
    m0 = float(input("Rest mass m0 (kg): "))

    print("KE =", KE(m0, v))



else:
    graph_choice = input(
        "That equation is not recognized. Do you want to see the Minkowski graph? (yes/no): "
    ).lower()

    if graph_choice == "yes":
        print("Loading graph...")

        import pygame
        import math

        pygame.init()

        W, H = 800, 800
        screen = pygame.display.set_mode((W, H))
        clock = pygame.time.Clock()

        CENTER = (W // 2, H // 2)
        SCALE = 35

        BLACK = (0, 0, 0)
        RED = (200, 0, 0)
        BLUE = (0, 0, 200)

        font = pygame.font.SysFont(None, 20)

        def to_screen(x, t):
            return (CENTER[0] + x * SCALE,
                    CENTER[1] - t * SCALE)

        def dist(p, q):
            return math.hypot(p[0] - q[0], p[1] - q[1])

        def vector_info(v):
            x, t = v
            angle = math.degrees(math.atan2(t, x))
            length = math.sqrt(x * x + t * t)
            return angle, length

        def draw_arrow(p1, p2, color):
            pygame.draw.line(screen, color, p1, p2, 3)

            angle = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
            size = 10

            left = (p2[0] - size * math.cos(angle - 0.5),
                    p2[1] - size * math.sin(angle - 0.5))
            right = (p2[0] - size * math.cos(angle + 0.5),
                     p2[1] - size * math.sin(angle + 0.5))

            pygame.draw.line(screen, color, p2, left, 2)
            pygame.draw.line(screen, color, p2, right, 2)

        yprime_dir = [1, 0.3]
        xprime_dir = [0.3, 1]

        dragging = None
        running = True

        while running:
            clock.tick(60)

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if dist(mouse, to_screen(*yprime_dir)) < 20:
                        dragging = "y"
                    elif dist(mouse, to_screen(*xprime_dir)) < 20:
                        dragging = "x"

                if event.type == pygame.MOUSEBUTTONUP:
                    dragging = None

            if dragging:
                mx, my = mouse
                mx = (mx - CENTER[0]) / SCALE
                my = -(my - CENTER[1]) / SCALE

                alpha = 0.2

                if dragging == "y":
                    yprime_dir[0] += (mx - yprime_dir[0]) * alpha
                    yprime_dir[1] += (my - yprime_dir[1]) * alpha

                elif dragging == "x":
                    xprime_dir[0] += (mx - xprime_dir[0]) * alpha
                    xprime_dir[1] += (my - xprime_dir[1]) * alpha

            screen.fill((255, 255, 255))

            for i in range(-10, 11):
                pygame.draw.line(screen, (220, 220, 220),
                                 to_screen(i, -10),
                                 to_screen(i, 10))
                pygame.draw.line(screen, (220, 220, 220),
                                 to_screen(-10, i),
                                 to_screen(10, i))

            for i in range(-10, 11):
                px, py = to_screen(i, 0)
                pygame.draw.line(screen, BLACK, (px, py - 5), (px, py + 5), 1)
                screen.blit(font.render(str(i), True, BLACK), (px - 5, py + 8))

                px, py = to_screen(0, i)
                pygame.draw.line(screen, BLACK, (px - 5, py), (px + 5, py), 1)
                screen.blit(font.render(str(i), True, BLACK), (px + 8, py - 5))

            pygame.draw.line(screen, BLACK,
                             to_screen(-10, 0),
                             to_screen(10, 0), 3)

            pygame.draw.line(screen, BLACK,
                             to_screen(0, -10),
                             to_screen(0, 10), 3)

            p0 = to_screen(0, 0)

            py = to_screen(*yprime_dir)
            px = to_screen(*xprime_dir)

            draw_arrow(p0, py, RED)
            draw_arrow(p0, px, BLUE)

            pygame.draw.circle(screen, RED, py, 6)
            pygame.draw.circle(screen, BLUE, px, 6)

            y_angle, y_len = vector_info(yprime_dir)
            x_angle, x_len = vector_info(xprime_dir)

            screen.blit(font.render(
                f"y' angle: {y_angle:.2f}°  length: {y_len:.2f}", True, RED), (10, 10))
            screen.blit(font.render(
                f"x' angle: {x_angle:.2f}°  length: {x_len:.2f}", True, BLUE), (10, 30))

            pygame.display.flip()

        pygame.quit()

    else:
        print("Check notes, or if you don't want to use it and learn special relativity then goodbye")

    #what we need now is COORDINATES, yes there is indeed coordinates in special relativity, the reason? When taking special relativity, it should be understood that two people will not agree on the same events, so to see when and where these events happen, we use coordinates, x' which I made blue, and y' which is red, we are only doing 2d, most highschool or basic special relativity courses rely on 2d graphs mostly, Im pretty sure actual full special relativity courses use 3d but we don't use it for simplicity and my code is just trash
    #what this code does, is to basically just have a normal coordinate plane, x,y all of that stuff we'd have since pre algebra when everyone was starting to discover variables, now we have that with xprime,yprime as a dialated frame, it isn't too good, this is 100% rushed and I have no idea how to use graphs so its centered around the origin, I just wanted this to teach basic special relativity.

#thank you for trying this out, I am open to any critism, this is my first project with Python so far for Hack Club.