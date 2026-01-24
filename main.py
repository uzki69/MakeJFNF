import os
import argparse
from pathlib import Path

def main():

    p = argparse.ArgumentParser("Links")
    p.add_argument("input", help="directory located files that will be linked", type=str)
    p.add_argument("output", help="directory where linked files will be", type=str)
    p.add_argument("title", help="tv show title", type=str)
    p.add_argument("season", help="tv show season", type=int)
    args = p.parse_args()

    filesToHandle: list[Path] = []

    if type(args.input) is str and type(args.output) is str and type(args.title) is str and type(args.season) is int:
        for entity in Path(args.input).iterdir(): 
            if entity.is_file():
                filesToHandle.append(entity)
        episode = 1
        outpath = Path(args.output)
        outpath = Path.joinpath(outpath, f"Season {args.season:02}")
        if not outpath.exists():
            outpath.mkdir(parents=True)
        for file in filesToHandle:
            handleVideo(file, outpath , args.title, args.season, episode)
            episode+=1

def handleVideo(video: Path, out: Path, title: str, season: int, ep: int):
    if not video.name.endswith(".mkv"):
        return
    
    name = f'{title} S{season:02}E{ep:02}.mkv'

    linkTo = Path.joinpath(out, name)

    os.symlink(video.absolute(), linkTo.absolute())


if __name__ == "__main__":
    main()