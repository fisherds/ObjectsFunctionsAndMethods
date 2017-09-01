"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Dave Fisher.
"""

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    # two_circles()
    # circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TO DO: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    circle = rg.Circle(rg.Point(200, 100), 50)
    circle.fill_color = 'green'
    circle.attach_to(window)

    circle2 = rg.Circle(rg.Point(50, 100), 30)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # TO DO: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    circle = rg.Circle(rg.Point(200, 175), 50)
    circle.fill_color = 'blue'
    circle.attach_to(window)

    rect = rg.Rectangle(rg.Point(25, 25), rg.Point(200, 100))
    rect.attach_to(window)

    print('circle outline_thickness', circle.outline_thickness)
    print('circle fill_color', circle.fill_color)
    print('circle center', circle.center)
    print('circle center.x', circle.center.x)
    print('circle center.y', circle.center.y)

    print('rect outline_thickness', rect.outline_thickness)
    print('rect fill_color', rect.fill_color)
    print('rect center', rect.get_center())
    print('rect center.x', rect.get_center().x)
    print('rect center.y', rect.get_center().y)

    window.render()
    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TO DO: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(300, 300)
    line1 = rg.Line(rg.Point(25, 25), rg.Point(200, 25))
    line1.attach_to(window)

    thicker_line = rg.Line(rg.Point(100, 100), rg.Point(250, 200))
    thicker_line.thickness = 10
    thicker_line.color = 'red'
    thicker_line.attach_to(window)

    print('midpoint', thicker_line.get_midpoint())
    print('midpoint.x', thicker_line.get_midpoint().x)
    print('midpoint.y', thicker_line.get_midpoint().y)

    window.render()
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
