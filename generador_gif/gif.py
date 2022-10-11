import imageio
preocupado = './preocupado.jpg'
serio = './pc_serio.png'
llorando = './llorando.jpg'
filenames =[preocupado, serio, llorando]

images = []

for filename in filenames:
  images.append(imageio.imread(filename))
  
imageio.mimsave('meme.gif', images, duration = 0.5)