import sys
import matplotlib.colors as mc
import matplotlib.pyplot as plt

class Solarized:
    def __init__(self):
        self.colors = {'base03':'#002b36',
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

    def cmap(self, type='listed'):
        """
        type: 'listed' or 'linear'
        """
        colors = ['yellow',
                  'orange',
                  'red',
                  'magenta',
                  'violet',
                  'blue',
                  'cyan',
                  'green']
            
        cpool = [self.colors[color] for color in colors]
        
        if type=='linear':
            cmap = mc.LinearSegmentedColormap.from_list('solarized', cpool)
        else:
            cmap = mc.ListedColormap(cpool, 'solarized')
            
        return cmap

def test_image(SolarizedObj, show=True):
    """
    Print a test image with listed and linear cmaps.
    """
    import numpy as np
    X = np.random.rand(20,20)

    fig = plt.figure(1)
    rect = fig.patch
    rect.set_facecolor(SolarizedObj.colors['base03'])

    ax = fig.add_subplot(121)
    ax.spines['left'].set_color(SolarizedObj.colors['base01'])
    ax.spines['bottom'].set_color(SolarizedObj.colors['base01'])
    ax.spines['top'].set_color(SolarizedObj.colors['base01'])
    ax.spines['right'].set_color(SolarizedObj.colors['base01'])
    ax.tick_params(axis='x', colors=SolarizedObj.colors['base01'])
    ax.tick_params(axis='y', colors=SolarizedObj.colors['base01'])
    plt.pcolor(X,cmap=SolarizedObj.cmap())
    c1 = plt.colorbar()
    c1.outline.set_visible(False)
    c1_ytick_obj = plt.getp(c1.ax.axes, 'yticklabels')                
    plt.setp(c1_ytick_obj, color=SolarizedObj.colors['base01'])

    ax2 = fig.add_subplot(122)
    ax2.spines['left'].set_color(SolarizedObj.colors['base01'])
    ax2.spines['bottom'].set_color(SolarizedObj.colors['base01'])
    ax2.spines['top'].set_color(SolarizedObj.colors['base01'])
    ax2.spines['right'].set_color(SolarizedObj.colors['base01'])
    ax2.tick_params(axis='x', colors=SolarizedObj.colors['base01'])
    ax2.tick_params(axis='y', colors=SolarizedObj.colors['base01'])
    plt.pcolor(X,cmap=SolarizedObj.cmap('linear'))
    c2 = plt.colorbar()
    c2.outline.set_visible(False)
    c2_ytick_obj = plt.getp(c2.ax.axes, 'yticklabels')                
    plt.setp(c2_ytick_obj, color=SolarizedObj.colors['base01'])

    if show:
        plt.show()
    else:
        fig.savefig('solarized.png',
                    facecolor=SolarizedObj.colors['base03'],
                    dpi=600)
    
def main():
    Sol = Solarized()
    test_image(Sol, False)

if __name__=='__main__':
    main()

    
