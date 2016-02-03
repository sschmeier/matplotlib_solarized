import matplotlib.colors as mc
import matplotlib.pyplot as plt

class Solarized:
    def __init__(self):
        self._color2hex = {'base03':'#002b36',
                           'base02':'#073642',
                           'base01':'#586e75',
                           'base00':'#657b83',
                           'base0':'#839496',
                           'base1':'#93a1a1',
                           'base2':'#eee8d5',
                           'base3':'#fdf6e3',
                           'yellow':'#b58900',
                           'orange':'#cb4b16',
                           'red':'#dc322f',
                           'magenta':'#d33682',
                           'violet':'#6c71c4',
                           'blue':'#268bd2',
                           'cyan':'#2aa198',
                           'green':'#859900'}

        self._accent_colors = ['yellow',
                               'orange',
                               'red',
                               'magenta',
                               'violet',
                               'blue',
                               'cyan',
                               'green']

    def get_accentcolors():
        """ Get a list of accent colors"""
        return self._accent_colors
        
    def color2hex(self, color):
        """ Convert a colorname to hex """
        color = color.lower()
        try:
            return self._color2hex[color]
        except KeyError:
            sys.stderr.write('Error: Not a solarized color.\n')
        
    def cmap(self, type='listed', indeces=[0,1,2,3,4,5,6,7]):
        """
        The cmap consists only of the 8 accent-colors:
        yellow, orange, red, ..., green.
        
        type: 'listed' or 'linear'
        indeces: list of indeces of accent colors to include in the colormap
        """
        colorpool = []
        indeces.sort()
        for i in indeces:
            if i in range(8):
                colorpool.append(self.color2hex(self._accent_colors[i]))
        if len(colorpool) < 1:
            return None

        if type=='linear':
            cmap = mc.LinearSegmentedColormap.from_list('solarized', colorpool)
        else:
            cmap = mc.ListedColormap(colorpool, 'solarized')
            
        return cmap

def test_image(SolarizedObj, show=True):
    """
    Print a test image with listed and linear cmaps.
    """
    Sol = SolarizedObj

    # create some random numbers on a 20 by 20 grid
    import numpy as np
    X = np.random.rand(20,20)

    fig = plt.figure(1)
    rect = fig.patch
    rect.set_facecolor(Sol.color2hex('base03'))

    ax = fig.add_subplot(121)
    ax.spines['left'].set_color(Sol.color2hex('base01'))
    ax.spines['bottom'].set_color(Sol.color2hex('base01'))
    ax.spines['top'].set_color(Sol.color2hex('base01'))
    ax.spines['right'].set_color(Sol.color2hex('base01'))
    ax.tick_params(axis='x', colors=Sol.color2hex('base01'))
    ax.tick_params(axis='y', colors=Sol.color2hex('base01'))
    plt.pcolor(X,cmap=Sol.cmap())
    c1 = plt.colorbar()
    c1.outline.set_visible(False)
    c1_ytick_obj = plt.getp(c1.ax.axes, 'yticklabels')                
    plt.setp(c1_ytick_obj, color=Sol.color2hex('base01'))

    ax2 = fig.add_subplot(122)
    ax2.spines['left'].set_color(Sol.color2hex('base01'))
    ax2.spines['bottom'].set_color(Sol.color2hex('base01'))
    ax2.spines['top'].set_color(Sol.color2hex('base01'))
    ax2.spines['right'].set_color(Sol.color2hex('base01'))
    ax2.tick_params(axis='x', colors=Sol.color2hex('base01'))
    ax2.tick_params(axis='y', colors=Sol.color2hex('base01'))
    plt.pcolor(X,cmap=Sol.cmap(type='linear'))
    c2 = plt.colorbar()
    c2.outline.set_visible(False)
    c2_ytick_obj = plt.getp(c2.ax.axes, 'yticklabels')                
    plt.setp(c2_ytick_obj, color=Sol.color2hex('base01'))

    if show:
        plt.show()
    else:
        fig.savefig('solarized.png',
                    facecolor=Sol.color2hex('base03'),
                    dpi=300)
    
def main():
    Sol = Solarized()
    test_image(Sol, False)

if __name__=='__main__':
    main()

    
