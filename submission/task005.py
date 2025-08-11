def solve(grid):
    import numpy as np
    
    # Convert to numpy array for easier manipulation
    inp = np.array(grid)
    out = inp.copy()
    h, w = inp.shape
    
    # Find all non-zero patterns
    rows, cols = np.where(inp != 0)
    
    if len(rows) == 0:
        return out.tolist()
    
    # Group pixels by value
    values = {}
    for r, c in zip(rows, cols):
        val = inp[r, c]
        if val not in values:
            values[val] = []
        values[val].append((r, c))
    
    # Find the template pattern (typically the largest/most complex pattern)
    template_val = None
    template_positions = None
    max_positions = 0
    
    for val, positions in values.items():
        if len(positions) > max_positions:
            max_positions = len(positions)
            template_val = val
            template_positions = positions
    
    if template_val is None:
        return out.tolist()
    
    # Get template bounding box and relative positions
    template_positions = sorted(template_positions)
    min_r = min(r for r, c in template_positions)
    min_c = min(c for r, c in template_positions)
    template_relative = [(r - min_r, c - min_c) for r, c in template_positions]
    
    # For each other pattern, apply template at each element's position
    for val, positions in values.items():
        if val == template_val:
            continue  # Skip the template itself
        
        # Check if this is a vertical line (extend horizontally)
        is_vertical_line = len(set(row for row, col in positions)) > 1 and len(set(col for row, col in positions)) == 1
        # Check if this is a horizontal line (extend vertically)  
        is_horizontal_line = len(set(row for row, col in positions)) == 1 and len(set(col for row, col in positions)) > 1
        
        # For each position in this pattern, apply template at base positions
        for r, c in positions:
            # Apply template at original position (offset 0)
            for dr, dc in template_relative:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < h and 0 <= new_c < w:
                    out[new_r, new_c] = val
            
            if is_vertical_line:
                # Vertical line - extend horizontally (every 4 columns)
                for offset in range(4, w, 4):
                    new_base_c = c + offset
                    if new_base_c >= w:
                        break
                    
                    # Place template pattern at this base position
                    for dr, dc in template_relative:
                        new_r, new_c = r + dr, new_base_c + dc
                        if 0 <= new_r < h and 0 <= new_c < w:
                            out[new_r, new_c] = val
                            
            elif is_horizontal_line:
                # Horizontal line - extend vertically (every 4 rows)
                for offset in range(4, h, 4):
                    new_base_r = r + offset
                    if new_base_r >= h:
                        break
                    
                    # Place template pattern at this base position
                    for dr, dc in template_relative:
                        new_r, new_c = new_base_r + dr, c + dc
                        if 0 <= new_r < h and 0 <= new_c < w:
                            out[new_r, new_c] = val
                            
            else:
                # Single points or other patterns - extend in both directions
                # Horizontal extension
                for offset in range(4, w, 4):
                    new_base_c = c + offset
                    if new_base_c >= w:
                        break
                    
                    for dr, dc in template_relative:
                        new_r, new_c = r + dr, new_base_c + dc
                        if 0 <= new_r < h and 0 <= new_c < w:
                            out[new_r, new_c] = val
                
                # Vertical extension  
                for offset in range(4, h, 4):
                    new_base_r = r + offset
                    if new_base_r >= h:
                        break
                    
                    for dr, dc in template_relative:
                        new_r, new_c = new_base_r + dr, c + dc
                        if 0 <= new_r < h and 0 <= new_c < w:
                            out[new_r, new_c] = val
    
    return out.tolist()
