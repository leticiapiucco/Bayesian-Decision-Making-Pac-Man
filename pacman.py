from game import *

if __name__ == '__main__':
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument("algorithm",
                        metavar="algorithm name",
                        help="'baeysian' or 'benchmark'")
    parser.add_argument('--ratio', required=False,
                        metavar="float number",
                        help='Ratio of whites to black tiles, eg. 0.6')
    parser.add_argument('--map', required=False,
                        metavar="map name",
                        help="Name of the map, e.g. classic")
    parser.add_argument('--ghosts', required=False,
                        metavar="number of ghosts",
                        help="Number of Ghosts, e.g. 25")


    args = parser.parse_args()
    game = None
    ratio = 0.55
    map = 'classic'
    ghosts = 25

    if args.algorithm != "benchmark" and args.algorithm != "bayesian":
        raise ValueError('Invalid algorithm.')    
    
    if args.ratio:
        ratio = float(args.ratio)
    
    if args.map:
        map = args.map
        
    if args.ghosts:
        ghosts = args.ghosts

    if args.algorithm == "benchmark":
        print("Benchmark algorithm starts")
        for i in range(5):
            game = Game(2, ratio, map, ghosts)
            game.run()
            while game.running:
                pass
    else:
        print("Bayesian algorithm starts")
        for i in range(5):
            game = Game(1, ratio, map, ghosts)
            game.run()
            while game.running:
                pass

