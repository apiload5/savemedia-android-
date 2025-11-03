def hex_to_rgba(hex_color, alpha=1.0):
    """Convert hex color to RGBA"""
    hex_color = hex_color.lstrip('#')
    hlen = len(hex_color)
    
    if hlen == 3:
        # Short format #RGB to #RRGGBB
        hex_color = ''.join([c*2 for c in hex_color])
        hlen = 6
    
    if hlen == 6:
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return (rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0, alpha)
    else:
        # Default to white if invalid
        return (1.0, 1.0, 1.0, alpha)

# Exact colors from savemedia.online website
COLORS = {
    # Main gradients
    "primary_gradient": ["#667eea", "#764ba2"],
    "dark_gradient": ["#2c3e50", "#3498db"],
    
    # Button colors
    "green_button": ["#4CAF50", "#45a049"],
    "blue_button": ["#2196F3", "#1976D2"], 
    "red_button": ["#e74c3c", "#c0392b"],
    "whatsapp_green": ["#25D366", "#128C7E"],
    
    # UI colors
    "white_transparent": "rgba(255,255,255,0.1)",
    "text_white": "#ffffff",
    "text_dark": "#333333",
    "text_gray": "#666666",
    "text_light": "#cccccc",
    
    # Background colors
    "card_light": "rgba(255,255,255,0.9)",
    "card_dark": "rgba(52,73,94,0.9)",
    
    # Status colors
    "success_green": "#27ae60",
    "error_red": "#e74c3c",
    "warning_orange": "#f39c12",
    "info_blue": "#3498db"
}
