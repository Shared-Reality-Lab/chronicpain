# Chronic Pain Exploratory Museum
A tool for people who experience chronic pain to be able to discover, create, and save art that they feel resonates with their pain. The purpose of developing a VR environment for this task is to allow users to fully immerse themselves in the art and focus solely on their pain and its connection to the art without the outside world there to distract them. Eventually, this environment will be compared to full in-person and partially in-person alternatives to study how immersion affects pain relief in Art Therapy. 

When the user enters the environment, they should be shown different art styles (starting very broad ex. an abstract piece, an impressionist piece, a realist piece, ...) and be able to "grade" the artworks on what aspects of the artworks they feel they resonate with. Then the software will suggest other paintings that they think the user would "grade" highly based on their past decisions.

The main goal of this project is for the user to be able to create a curation of artworks that they feel represent their pain. This curation can then be shown to family members and doctors so they can hopefully gain a better understanding of the pain the user experiences.

## Building to Meta Quest 2 Headset
Before attempting to build the project to the headset, make sure developer mode is enabled in the headset (this can be found in the headset Settings). There are three methods to build a Unity project to the headset: two options for development on a Windows PC and last for development on a Mac. To build off a Windows PC you can use either Air Link or Meta Quest Link (using meta's Link cable). 

To use Air Link, ensure that your PC and the headset are on the same wifi network, and that both wifi connections are strong. For Meta Quest Link connection, plug in the Link cable to your PC and the headset. Using this method you do not need to create a build of the project, the Unity Game mode will automatically be cast to the headset.

For development on Mac, plug any high speed power and data USB C to USB C cable into your PC and the headset. Most Apple charging cables should work. Go to File > Build Settings... and make sure the following options are selected:

- **Platform:** Android (Unity symbol indicates which platform is selected)
- **Run Device:** Meta Quest 2

Once the build to the Meta Quest 2 is complete, it should be available in the headset under your personal applications. 

Additionally, when building for VR headset, make sure to comment out the Player game component (used for Game mode on computer) and comment in the XR Interaction Setup game component (used for Game mode on VR headset). 

## Samples of OpenAI Implementation
The OpenAI Unity Package (https://github.com/srcnalt/OpenAI-Unity) is used to handle all interactions with OpenAI. The package provides sample scenes which show how the features can be implemented. The example for Whisper (speech-to-text ML model) can be found under Samples > OpenAIUnity > 0.2.0 > Whisper > Whisper Sample. The example for DallE (image in-painting and generation ML model) can be found under Samples > OpenAIUnity > 0.2.0 > DallE > DallE Sample. 

When either of these scenes are clicked upon, developers can see components used to build this feature which they can then use as guidance when developing new features.
