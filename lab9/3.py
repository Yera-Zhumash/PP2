import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15  # Default brush size
    mode = 'blue'  # Default color mode
    drawing_tool = 'line'  # Default drawing tool
    shape_start_pos = None  # Store the starting position for shapes
    points = []  # Store points for freehand drawing
    trail_points = []  # Store points for mouse trail mode
    
    drawing_surface = pygame.Surface((640, 480))
    drawing_surface.fill((0, 0, 0))  # Black background
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Color selection
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
                
                # Tool selection
                elif event.key == pygame.K_e:
                    drawing_tool = 'eraser'
                elif event.key == pygame.K_l:
                    drawing_tool = 'line'
                elif event.key == pygame.K_s:
                    drawing_tool = 'square'
                elif event.key == pygame.K_t:
                    drawing_tool = 'right_triangle'
                elif event.key == pygame.K_u:
                    drawing_tool = 'equilateral_triangle'
                elif event.key == pygame.K_d:
                    drawing_tool = 'rhombus'
                elif event.key == pygame.K_p:
                    drawing_tool = 'trail'
                    trail_points = []
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Click
                    if drawing_tool in ['square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        shape_start_pos = event.pos  # Store start position
                    elif drawing_tool in ['line', 'eraser', 'trail']:
                        radius = min(200, radius + 1)  # Increase size
                elif event.button == 3:  # Right Click
                    radius = max(1, radius - 1)  # Decrease size
            
            if event.type == pygame.MOUSEMOTION:
                if drawing_tool == 'eraser':
                    pygame.draw.circle(drawing_surface, (0, 0, 0), event.pos, radius)
                elif drawing_tool == 'line':
                    position = event.pos
                    points.append(position)
                    points = points[-100:]
                elif drawing_tool == 'trail':
                    trail_points.append(event.pos)
                    if len(trail_points) > 100:
                        trail_points.pop(0)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if drawing_tool in ['square', 'right_triangle', 'equilateral_triangle', 'rhombus'] and shape_start_pos:
                    end_pos = event.pos
                    if drawing_tool == 'square':
                        width = abs(end_pos[0] - shape_start_pos[0])
                        height = abs(end_pos[1] - shape_start_pos[1])
                        pygame.draw.rect(drawing_surface, get_color(mode), (shape_start_pos[0], shape_start_pos[1], width, height), 2)
                    elif drawing_tool == 'right_triangle':
                        pygame.draw.polygon(drawing_surface, get_color(mode), [shape_start_pos, (shape_start_pos[0], end_pos[1]), end_pos], 2)
                    elif drawing_tool == 'equilateral_triangle':
                        side_length = abs(end_pos[0] - shape_start_pos[0])
                        height = side_length * (3 ** 0.5) / 2
                        pygame.draw.polygon(drawing_surface, get_color(mode), [shape_start_pos, (shape_start_pos[0] + side_length, shape_start_pos[1]), (shape_start_pos[0] + side_length / 2, shape_start_pos[1] - height)], 2)
                    elif drawing_tool == 'rhombus':
                        mid_x = (shape_start_pos[0] + end_pos[0]) / 2
                        mid_y = (shape_start_pos[1] + end_pos[1]) / 2
                        pygame.draw.polygon(drawing_surface, get_color(mode), [(mid_x, shape_start_pos[1]), (end_pos[0], mid_y), (mid_x, end_pos[1]), (shape_start_pos[0], mid_y)], 2)
                    shape_start_pos = None
        
        screen.fill((0, 0, 0))
        screen.blit(drawing_surface, (0, 0))
        
        if drawing_tool == 'line':
            for i in range(len(points) - 1):
                drawLineBetween(drawing_surface, i, points[i], points[i + 1], radius, mode)
        
        if drawing_tool == 'trail':
            for point in trail_points:
                pygame.draw.circle(drawing_surface, get_color(mode), point, radius)
            if len(trail_points) > 0:
                trail_points.pop(0)
        
        pygame.display.flip()
        clock.tick(60)

def get_color(mode):
    colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'yellow': (255, 255, 0), 'white': (255, 255, 255)}
    return colors.get(mode, (255, 255, 255))

def drawLineBetween(screen, index, start, end, width, color_mode):
    color = get_color(color_mode)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = i / iterations
        x = int(start[0] * (1 - progress) + end[0] * progress)
        y = int(start[1] * (1 - progress) + end[1] * progress)
        pygame.draw.circle(screen, color, (x, y), width)

main()
