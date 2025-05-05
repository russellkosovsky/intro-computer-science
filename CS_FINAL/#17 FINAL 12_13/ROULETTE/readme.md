(4 points) a clear statement of the project
(8 points) description of the major components of the design, particularly the classes and methods (including parameters and return types)
(3 points) kinds of testing you have done and modifications you would make for a future version
You also need to list up all resources you used. Anything that is not your work in the project must be cited.


The goal of the project was to develop a functioning game of roulette, a casino game, where a ball spins around a wheel and players pick where they think the ball will land. In our proposal, we wanted a functioning wheel, and buttons to act as betting pieces, where a random number would be generated. If the users bet placement was correct, they were a winner. We also wanted the user to play as many times as possible

During our proposal we originally wanted a spinning .png file, that we got online. Unfortunately after several attempts with turtle.py , and pillow.py, we decided to use a graphically control wheel instead

The main compenents of the roullete game itself, include the GUI which has the basic elements of a wheel drawn to the users screen via layering, as well as a pollygon arrow, with 36 circles going around the circumfrnece of the center circle representing each possible outcome of the spin.

The spin was tricky, we originially had a random number between 0,36 get drawn to a circle highlighting it in white, representing the marble. But we realized it was very bland, so we decided to simulate a spin, by drawing each circle over one another. This turned out really nice, as eventually, we added to the animation, and had a single circle get drawn when the player hits spin. Using conditionals, the value of the randomly generated number would align with the users selection via the getLabel command. If the user picked correctly, we added the winnings to the users wallet. 

After that, we moved everything into classes, making it very easy to call seperate functions. This also made the program alot faster........ADD ON CLASSES HERE.....

Throughout the project we would always print() both the generating number and color, as well as the number and color of the users selection. this made it easy to track down bugs we had. One of the biggest ones, was getting the money to properly display to the entry box at the top. The reason we used an entry box was because, it seemed to fit the aesthetic of an online casino rather than print. Fortunately any edits to the box are not saved to avoid cheating. Tests done to the img file, are in the test folder, where we tried various ways of moving and rotating an image, but in the long run we are glad that we choose a graphicly enabled wheel rather than a picture, allowing more customization......ADD TO TESTING HERE.....

For audio, we used the elements of lab 12 using wavmod.py , we then found a website called https://mixkit.co/free-sound-effects/. This wes a royalty free audio cite, where we were able to get retro arcade sounds for each button click. As for the intro, we used uberduck which is a AI voice generator "text-speech". https://uberduck.ai/

