import shutil
import textwrap
import time

ASCII_ART = r""" 
   ____    __    ____  _______  __        ______   ______   .___  ___.  _______                   
   \   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|                  
    \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__                     
     \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|                    
      \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____                   
       \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|                  
                                                                                                  
         .___________.  ______                                                                    
         |           | /  __  \                                                                   
         `---|  |----`|  |  |  |                                                                  
             |  |     |  |  |  |                                                                  
             |  |     |  `--'  |                                                                  
             |__|      \______/                                                                   
                                                                                                  
   .___________..______          ___       ______  __  ___  __       __       _______.___________.
   |           ||   _  \        /   \     /      ||  |/  / |  |     |  |     /       |           |
   `---|  |----`|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |     |  |    |   (----`---|  |----`
       |  |     |      /      /  /_\  \  |  |     |    <   |  |     |  |     \   \       |  |     
       |  |     |  |\  \----./  _____  \ |  `----.|  .  \  |  `----.|  | .----)   |      |  |     
       |__|     | _| `._____/__/     \__\ \______||__|\__\ |_______||__| |_______/       |__|     
                                                                                                                                                                                                                                          
"""
DESCRIPTION = (
    "Tip: For the best experience, maximize your terminal or command prompt window.")



def get_terminal_width(default=100):
    try:
        return shutil.get_terminal_size((default, 30)).columns
    except Exception:
        return default

def responsive_art_block(art_block, term_w, margin=2):
    allowed = max(10, term_w - margin)
    out = []
    for raw in art_block.splitlines():
        line = raw.rstrip("\n")
        if not line.strip():
            out.append("".center(term_w))
            continue
        if len(line) <= allowed:
            out.append(line.center(term_w))
        else:
            out.append(line[:allowed].center(term_w))
    return "\n".join(out)



def main():
    term_w = get_terminal_width()
    print()
    print(responsive_art_block(ASCII_ART, term_w))
    print()
    time.sleep(2)
    for char in DESCRIPTION:
        print(char, end='', flush=True)
        if char in '.!?':
            time.sleep(0.3)
        else:
            time.sleep(0.05)
    print()


if __name__ == "__main__":
    main()