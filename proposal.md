# Proposal

## What will (likely) be the title of your project?

AutoMod Plus+

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

The twitch AutoMod only holds chats for review from the streamer/moderator, but does not take action against the user that triggered the hold of that specific chat. I want this bot to be able to automatically ban/kick/timeout a user given that a certain frase or word is used, to see if this is possible.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

As I said above, I want this bot to be able to automatically ban, kick or timeout a user based on their usage of a blacklisted word frase or symbol. I want to have a list of blacklisted items that can be updated by the user. This bot will monitor every message sent into the chat and go through each string word by word and see if it matches anything in the blacklist. If it does, the bot (given that it has moderator privileges, so I will likely have to link it to its own twitch account) will send a message into the chat to either @ the user with a warning, or take action in terms of banning/time out/kick. Because all of these actions can be done through the chat, I believe that this is doable. If there is time, I would also like it to have a warning feature that gives a certain number of warnings before taking action. This would require it to take into account how many times a certain user has been warned.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

N/A

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

A good outcome would be having a code that works in theory, that, if I am able to link it to a twitch moderator account, would have the ability to ban a user for saying a certain word. 

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

A better outcome would include the previous outcome + the bot's ability to look for phrases, and be able to differentiate between having to kick or timeout someone and having to ban them.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

the BEST outcome would be the above two features, plus the bot's ability to use a warning system, and keep track of how many warnings have been issued to the user before finally taking action. Best case, the owner of the bot would be able to look back at the logs for a certain user with a list of warnings/offenses and why the warnings were issued.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

I'll first need to figure out how I can connect this code to a bot and then connect it to a twitch account. I need to research how to connect bots to twitch accounts and how that works in terms of automating an account. After that, I'll need to see if it would be easier to somehow implement the bot directly into the user's own twitch account instead of it being an outside source (probably wouldn't be easier, but I'll look into it). 
