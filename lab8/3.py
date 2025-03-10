import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'  # Default color mode
    drawing_tool = 'line'  # Default drawing tool
    shape_start_pos = None  # Store the starting position for shapes (rectangle/circle)
    points = []  # Store points for freehand drawing (line/eraser)
    shapes = []  # Store shapes (rectangles and circles)
    trail_points = []  # Store points for mouse trail mode
    
    # Create a separate surface for drawing
    drawing_surface = pygame.Surface((640, 480))
    drawing_surface.fill((0, 0, 0))  # Initialize with black background
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # Determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Determine if a letter key was pressed for color or tool selection
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'
                elif event.key == pygame.K_w:
                    mode = 'white'
                elif event.key == pygame.K_e:
                    drawing_tool = 'eraser'
                elif event.key == pygame.K_l:
                    drawing_tool = 'line'
                elif event.key == pygame.K_c:
                    drawing_tool = 'circle'
                elif event.key == pygame.K_s:
                    drawing_tool = 'rectangle'
                elif event.key == pygame.K_p:
                    drawing_tool = 'trail'  # Switch to mouse trail mode
                    trail_points = []  # Clear the trail when switching to trail mode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if drawing_tool in ['rectangle', 'circle']:
                        shape_start_pos = event.pos  # Store the starting position for shapes
                    elif drawing_tool in ['line', 'eraser', 'trail']:
                        radius = min(200, radius + 1)  # Increase radius for line/eraser/trail
                elif event.button == 3:  # Right click
                    radius = max(1, radius - 1)  # Decrease radius
            
            if event.type == pygame.MOUSEMOTION:
                if drawing_tool == 'eraser':
                    # Erase by drawing black circles directly on the drawing surface
                    pygame.draw.circle(drawing_surface, (0, 0, 0), event.pos, radius)
                elif drawing_tool == 'line':
                    # If mouse moved, add point to list (for line mode)
                    position = event.pos
                    points = points + [position]
                    points = points[-73:]  # Limit the number of points to 73 (256 / 3.5 ≈ 73)
                elif drawing_tool == 'trail':
                    # Add the current mouse position to the trail points
                    trail_points.append(event.pos)
                    trail_points = trail_points[-100:]  # Limit the number of trail points
            
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_tool in ['rectangle', 'circle'] and shape_start_pos:
                    # Draw the shape when the mouse button is released
                    if drawing_tool == 'rectangle':
                        width = abs(event.pos[0] - shape_start_pos[0])
                        height = abs(event.pos[1] - shape_start_pos[1])
                        top_left = (min(shape_start_pos[0], event.pos[0]), min(shape_start_pos[1], event.pos[1]))
                        pygame.draw.rect(drawing_surface, get_color(mode), (top_left[0], top_left[1], width, height), radius)
                    elif drawing_tool == 'circle':
                        center = shape_start_pos
                        radius_shape = int(((event.pos[0] - shape_start_pos[0]) ** 2 + (event.pos[1] - shape_start_pos[1]) ** 2) ** 0.5)
                        pygame.draw.circle(drawing_surface, get_color(mode), center, radius_shape, radius)
                    shape_start_pos = None  # Reset the starting position
        
        # Clear the screen with black
        screen.fill((0, 0, 0))
        
        # Draw the drawing surface onto the screen
        screen.blit(drawing_surface, (0, 0))
        
        # Draw all points (for line mode)
        if drawing_tool == 'line':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(drawing_surface, i, points[i], points[i + 1], radius, mode)
                i += 1
        
        # Draw trail points (for mouse trail mode)
        if drawing_tool == 'trail':
            for point in trail_points:
                pygame.draw.circle(drawing_surface, get_color(mode), point, radius)
            # Remove the oldest point to make the trail vanish over time
            if len(trail_points) > 0:
                trail_points.pop(0)
        
        pygame.display.flip()
        clock.tick(60)

def get_color(mode):
    # Return the color based on the mode
    if mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'blue':
        return (0, 0, 255)
    elif mode == 'yellow':
        return (255, 255, 0)
    elif mode == 'white':
        return (255, 255, 255)
    elif mode == 'black':
        return (0, 0, 0)
    else:
        return (0, 0, 0)

def drawLineBetween(screen, index, start, end, width, color_mode):
    # Draw a line between two points with a gradient effect
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    color = get_color(color_mode)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()