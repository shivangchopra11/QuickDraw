# QuickDraw
Can a neural network learn to recognize doodling? [Quick, Draw](https://quickdraw.withgoogle.com/)

### Description
Quick, Draw! is an online game developed by Google that challenges players to draw a picture of an object or idea and then uses a neural network artificial intelligence to guess what the drawings represent. The AI learns from each drawing, increasing its ability to guess correctly in the future.The game is similar to Pictionary in that the player only has a limited time to draw (20 seconds).The concepts that it guesses can be simple, like 'foot', or more complicated, like 'animal migration'. This game is one of many simple games created by Google that are AI based as part of a project known as 'A.I. Experiments'. [Quick, Draw](https://quickdraw.withgoogle.com/)

### Dataset
Follow the documentation [here](https://github.com/googlecreativelab/quickdraw-dataset) to get the dataset. I got `.npy` files from google cloud for 4 drawings for the CNN part of the network and `.ndjson`  files of the same drawings for the LSTM part.

### Labels
1) Alarm Clock: ⏰ 
2) Cloud: 🌧️ 
3) Book: 📚
4) Campfire: 🔥

### Demo
![Alt text](https://github.com/shivangchopra11/QuickDraw/blob/master/Gif%20P1.gif)

![Alt text](https://github.com/shivangchopra11/QuickDraw/blob/master/Gif%20P2.gif)

### References:
 
 - [Google's Quick, Draw](https://quickdraw.withgoogle.com/) 
 - [The Quick, Draw! Dataset](https://github.com/googlecreativelab/quickdraw-dataset)
 - [Quick Draw: the world’s largest doodle dataset](https://towardsdatascience.com/quick-draw-the-worlds-largest-doodle-dataset-823c22ffce6b)

### Future Work
As of now, the LSTM starts predicting the drawing after it has recorded 100 points of the drawing. This can be optimised to provide padded input to the LSTM network and give predictions once the prediction confidence crosses a certain threshold.

