# Stanford Code in Place Art Exhibit Experiment

![Process Photo GitHub Action](https://action-badges.now.sh/KatherineMichel/stanford-code-in-place-art-exhibit-experiment)

## Introduction

For my [Stanford Code in Place Final Project](https://github.com/KatherineMichel/stanford-code-in-place-final-project), I created a program that downloads a random pet photo from the Unsplash curated "Personable Pets" collection, modifies it with a randomly chosen image filter algorithm, and tweets the image on the [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account.

As I looked through the thousands of images that were tweeted, I was awestruck by one in particular that I thought looked like a piece of artwork. It hadn't crossed my mind that I would accidentally create artwork. 

This gave me the idea to set up another bot to intentionally create algorithmically generated artwork. 

In this repo, I have set up a similar bot called the [Stanford CiP (Code in Place) Art Bot](https://twitter.com/StanfordCiPArt). For the time being, this bot will apply the "negative" algorithm to photos that are interesting to me. I chose the "negative" algorithm because in my opinion, it is most likely to create an artistic effect. I will curate the photos I believe to be the most aesthetically pleasing into a small art exhibit.

Having never thought of this idea before, I have no idea if it would be of interested to people who enjoy traditional art or if it would be considered some sort of sacrilege. 

My intention would not be to "replace" traditional artwork. Artwork often reflects the human condition. That, by its very nature, simply cannot be replicated by a computer. I think paradoxically, by looking at artwork created by an algorithm, we can actually further examine and appreciate what the purpose and value of traditional artwork is. 

My own belief is that "art" can mean many things. I have heard it be said that there is an "art and a science" to computer programming. The better I understand, the more I believe this to be true because of the decision-making and creativity involved. 

My exhibit will be about the joy in building, inventing, discovering, and sharing, including "accidental" artwork. 

### Special Info

Table of Contents
-----------------

* [Connect](#connect)
* [Exhibit Photos](#exhibit-photos)
* [About](#about)
  * [Unsplash API](#unsplash-api)
  * [Photo Sources Used](#photo-sources-used)
  * [Other Possible Photo Sources](#other-possible-photo-sources)
<!--
* [Exhibit](#exhibit)
  * [Possible Galleries](#possible-galleries)
  * [Publicity](#publicity)
* [Additional Resources](#additional-resources)
* [Demo Videos](#demo-videos)
  * [Short Demo Agenda](#short-demo-agenda)
  * [Long Demo Agenda](#long-demo-agenda)
-->
* [Inspiration](#inspiration)
* [Change Log](#change-log)
* [Milestones](#milestones)
* [Code of Conduct](#code-of-conduct)
* [Copyright](#copyright)

## Connect

## Exhibit Photos

![](demo-photos/favorite-negative.jpg)

### Favorites

* https://twitter.com/StanfordCiPArt/status/1269180119077154817 
* https://twitter.com/StanfordCiPArt/status/1269706410641764359

## About
  
This exhibit could be viewed online or in person.

### Unsplash API

https://source.unsplash.com/

### Photos Sources Used

* https://unsplash.com/collections/461104/the-deep-(beneath-still-waters)
* https://unsplash.com/collections/1262111/marine
* https://unsplash.com/collections/1245/sea
* https://unsplash.com/collections/181581/animals

### Other Possible Photo Sources

Collections
* TBD

Key Words
* https://unsplash.com/s/photos/wildlife
* https://unsplash.com/backgrounds/art/aquarium
* https://unsplash.com/s/photos/under-the-sea
* https://unsplash.com/s/photos/sea
* https://unsplash.com/images/animals
* https://unsplash.com/s/photos/underwater
* https://unsplash.com/images/animals/fish
* https://unsplash.com/s/photos/jellyfish
* https://unsplash.com/s/photos/marine-life
* https://unsplash.com/s/photos/marine
* https://unsplash.com/s/photos/sealife
* https://unsplash.com/s/photos/mammal
* https://unsplash.com/s/photos/reef
* https://unsplash.com/s/photos/creature

<!--
## Exhibit

### Possible Galleries

A list of possible art galleries to approach to do a small exhibit. 

* [Wichita Art Museum](https://www.wichitaartmuseum.org/)
* [Hutchinson Art Center](https://www.hutchinsonartcenter.net/)
* [Hutchinson Chamber Art Gallery](https://www.hutchgov.com/1225/Chamber-Art-Gallery)
* [Stone House Gallery](https://www.fredoniakschamber.org/the-stone-house-gallery.html)

https://www.wichitaartmuseum.org/programs_events/calendar

### Publicity

## Additional Resources

## Demo Videos

### Short Demo Agenda

### Long Demo Agenda
-->

## Inspiration

This project was inspired by a few other projects
* [Jessica Garson's PyCon 2019 talk "Making Music with Python, SuperCollider and FoxDot"](https://youtu.be/YUIPcXduR8E)
* [Joanne Hastie's PyCascades 2020 "Programming a robot arm to paint: successes & happy accidents"](https://2020.pycascades.com/talks/programming-a-robot-arm-to-paint-successes-and-happy-accidents/)

## Change Log

### March 21, 2021

* Set bot to "Marine" photo collection

### July 16, 2020

* Set bot to "The Deep (Beneath Still Waters)" photo collection

### June 10, 2020

* Set bot to "Marine" photo collection

### June 8, 2020

* Set cron job to every 15 minutes

### June 7, 2020

* Added "Inspiration" section

### June 6, 2020

* Remove random URL generation (Unsplash automatically returns a random photo)
* Remove unused algorithms
* Add `pass` statement in case the file already exists
* Use black to format file
* Add "build passing" badge

### June 5, 2020

* Get bot up and running
* Set bot to use "Negative" Algorithm only
* Set bot to use "The Deep (Beneath Still Waters)" photo collection
* Began building out README.md

## Milestones

- [X] Set up a basic README.md
- [X] Choose possible photo sources
- [X] Get the bot up and running
- [X] Start curating photos

## Code of Conduct

Those who engage with this project are expected to follow my [Code of Conduct](https://github.com/KatherineMichel/.github/blob/master/CODE_OF_CONDUCT.md). 

## Copyright

© 2020-Present Katherine Michel. All Rights Reserved.

:top: <sub>[**Back to Top**](#table-of-contents)</sub>
