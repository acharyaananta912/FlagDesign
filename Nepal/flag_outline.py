def make_outline(width):
  # A width of a flag was given as an input (AB = width)
  # Height of the flag is 4/3*width (AC = height)
  height = 4/3*width

  # the vertical line of a flag extends from 0 to height, x = 0, only y varies (vertical line x = vlx, vertical line y = vly)
  # similarly the lower horizontal line extends from 0 to width, (horizontal lower line x = hllx, horizontal lower line y = hlly)
  vly = np.arange(0, height, 0.01)
  vlx = np.zeros(len(vly))

  hllx = np.arange(0,width,0.01)
  hlly = np.zeros(len(hllx))

  # Now we need slant line to the bottom. The slant line is extended from the lower right corner upto the length of width in the height
  # i.e slant line: x = 0 to width, y = -1*x + width (AD = width, BD = sqrt(2)*width)
  # but we want only a section of BD; i.e BE = width, ED = (sqrt(2)-1)*width
  # Now we drop perpendicular line from E towards AD and AB and mark it as EF and EG respectively
  # EF = (sqrt(2)-1)*width/sqrt(2)
  # EG = AF = AD - DF = AD - EF = width ( 1 - (sqrt(2)-1)/sqrt(2))

  # the lower slant line extends from width * (sqrt(2)-1)/sqrt(2) to the width
  # slant lower line x (sllx), slant lower line y (slly)
  sllx = np.arange(((np.sqrt(2)-1)/np.sqrt(2))*width, width, 0.01)
  slly = -1 * sllx + width # y = mx + c; m = -1, c = width

  # upper horizontal line x will start from the same point where sllx started and ended 
  # y will start from width*(sqrt(2) - sqrt(2) + 1)/sqrt(2) = width/sqrt(2)
  # upper horizontal line x: sllx (same as above)
  # upper horizontal line y: uhly
  uhly = np.ones(len(sllx))*width/np.sqrt(2)

  # upper slanted line goes from the top of the height to the base of upper horizontal line
  # x: 0 to width
  # y = mx + c; m = tan(A) = 1/3*width + (sqrt(2)-1)/sqrt(2)*width = (sqrt(2) + 3*sqrt(2) - 3)/(3*sqrt(2))*width = width*(4*sqrt(2)-3)
  # x: same as hllx
  # upper slant line y (suly)
  suly = -((4 * np.sqrt(2) - 3) /(3* np.sqrt(2))) * hllx + height

  plt.figure(figsize=(height, width))
  plt.gca().set_aspect('equal', adjustable='box')

  plt.plot(vlx, vly, "-b")
  plt.plot(hllx, hlly,"-b")
  plt.plot(sllx, slly,"-b")
  plt.plot(sllx, uhly,"-b")
  plt.plot(hllx, suly,"-b")
  plt.axis('off')
  plt.savefig("flag_outline.png")

