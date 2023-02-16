<script setup>
import router from '../routes/index.js';

function returnToHome() {
  router.push("/")
}

const images = [
  {
    src: 'src/assets/carousel/Carousel1.png'
  }, {
    src: 'src/assets/carousel/Carousel2.png'
  }, {
    src: 'src/assets/carousel/Carousel-3.png'
  }, {
    src: 'src/assets/carousel/Carousel4.png'
  }, {
    src: 'src/assets/carousel/Carousel5.png'
  },
]
</script>

<template>
  <div style="background-color: #f5f7f8;">

    <v-carousel
        :show-arrows="true">
      <v-carousel-item

          v-for="(image, i) in images"
          :key="i"
          :src="image.src"
          cover
          style="position: relative;">
        <img :src="image.src" alt="image" style="width: 100%; height: 100%; object-fit: cover;"/>
        <v-sheet
            v-if="i!==0"
            color="transparent"
            style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center;">
          <div class="text-h2 carousel-title">
            iFeed
          </div>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>

    <v-container class="bg-surface-variant " style="height: 100%">
      <v-btn
          color="primary"
          icon="mdi-home"
          size="x-large"
          @click="returnToHome()"
      >
      </v-btn>
      <v-row no-gutters>
        <v-col md="12">
          <h2 class="text-center pb-2 text-md-h2 ">Introducing iFeed:</h2>
          <p class="">Do you have a cat or dog? If yes, iFeed is the go to for you.
            With iFeed, you can rest assured that your pet is correctly fed, even when you are away at
            work or on holidays.
            You can easily set the amount of food and the eating time and leave the rest to us. You can
            monitor your pet's eating activity through a live video feed.
            The food will automatically dispense and alert your pet by calling their name.</p>
        </v-col>
      </v-row>

      <v-row class="pt-4">
        <v-col cols="12" md="8">
          <div class="pt-10">
            <v-card variant="outlined">
              <v-card-title>
                <p class="text-md-h4">What Makes The Product Different:</p>
              </v-card-title>
              <v-card-text class="p-2">
                <ul>
                  <li>A weight sensor accurately measures to the gram the amount of food to be
                    dispensed. There are reliable counter measures to prevent inaccuracies and a robust design
                    ensures its stability and reliability.
                  </li>
                  <li>
                    Your scheduling details are sent fast and securely to the food dispenser (more details
                    on technical insight section).
                  </li>
                  <li>
                    A camera that allows the user to monitor the pets’ eating activity and ensure that
                    the correct pet has come to eat.
                  </li>
                  <li>
                    A speaker calls your pet by its name to alert them that the food is ready!
                  </li>
                  <li>
                    You can also use our product physically by setting the proper food amount with the
                    physical keypad.
                  </li>
                </ul>
              </v-card-text>
            </v-card>
          </div>
        </v-col>

        <v-col cols="12" md="4">
          <div class="d-flex justify-center mt-4">
            <img alt="image" src="../assets/product.jpg" style="max-width: 100%;">
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" md="6">
          <div class="d-flex justify-center mb-4">
            <img alt="image" src="../assets/FormImage.png" style="max-width: 100%;">
          </div>
        </v-col>

        <v-col cols="12" md="6">
          <v-card variant="outlined">
            <v-card-title class="text-center text-md-h4 pa-2 ma-2 ">
              How To Use The Website
            </v-card-title>
            <v-card-text>
              <ul>
                <li>
                  You simply create an account and create the profiles of your pets.
                </li>
                <li>
                  In order to use iFeed, you set the feeding schedules; that’s it! You are done!
                </li>
                <li>
                  You can also choose the same schedule be repeated for every day or every week.
                </li>
              </ul>
            </v-card-text>
          </v-card>

          <div class="d-flex justify-center mt-4">
            <img alt="image" src="../assets/homeImage.png" style="max-width: 100%;">
          </div>
        </v-col>
      </v-row>


      <!--    Echo friendly-->
      <v-row>
        <v-col cols="12" md="8">
          <div class="pa-2 ma-2 pt-8 pt-md-16">
            <v-card variant="outlined">
              <v-card-title>
                <p class="text-center text-md-h4">Echo friendly</p>
              </v-card-title>
              <v-card-text>
                <ul>
                  <li>
                    If you do not want to use the product anymore, you can return it to us, and we will
                    reuse the material. Otherwise, do not forget to recycle it to help the
                    environment.
                  </li>
                </ul>
              </v-card-text>
            </v-card>
          </div>
        </v-col>
        <v-col class="text-center" cols="12" md="4">
          <img alt="image" class="image" src="../assets/eco-friendly.png" style="max-width: 200px">
        </v-col>
      </v-row>

      <!--    Tech Details-->
      <v-row>
        <v-col cols="12" md="12">
          <div class="pa-2 ma-2">
            <v-card variant="outlined">
              <v-card-title>
                <p class="text-center text-md-h4">Technical Details:</p>
              </v-card-title>
              <v-card-text>
                <div>
                  <ul>
                    <li>
                      The Front-end runs on Vue and the backend on python. They communicate through
                      the FastAPI library.
                    </li>
                    <li>
                      A Raspberry Pi controls the DC motor, the servo motor, the weight sensor, the
                      camera, the speaker, and the keypad.
                    </li>
                    <li>
                      MQTT is used with SSL encryption for the communication between the RPi and the
                      web app.
                    </li>
                    <li>
                      A DC motor is used to start spinning the fan on demand for the appropriate amount
                      of food to be prepared for dispensing. Its movement prevents from any food to get stuck.
                      The high speed of the motor results in a fast food-delivery.
                    </li>
                    <li>
                      A servo motor lifts a platform to dispense the food onto the bowl. It is limited to the
                      arc of a half-circle to prevent food from getting stuck in the dispensing fan.
                    </li>
                    <li>
                      The weight sensor uses a moving-average median window to account for inaccurate
                      sensor readings.
                    </li>
                  </ul>
                </div>
              </v-card-text>
            </v-card>
          </div>
        </v-col>
      </v-row>
      <!--Commercial-->
      <v-row>
        <v-col cols="12" md="12">
          <div class="text-center">
            <iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen height="800"
                    src="https://www.youtube.com/embed/IjUVcGiicWI"
                    title="Tr&amp;eacute;ning TEXT" width="100%"></iframe>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <!--  </v-parallax>-->
  </div>
</template>


<style scoped>

.carousel-title {
  font-size: 58px;
  font-weight: 300;
  line-height: 1.2;
  letter-spacing: -0.020em;
  color: #fff;
  text-align: center;
}

p, li {
  font-size: large;
  /*font-family: "Roboto";*/
  color: black;
  font-weight: bold;
}

h2 {
  color: black;

}

:deep(.v-row) {
  padding-top: 70px;

}

:deep(.v-card) {
  background: white;
  border-radius: 15px;
}

.image {
  width: 300px;
}


ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

li {
  margin-bottom: 10px;
  position: relative;
  padding-left: 20px;
}

li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #b7c0d5;
  /*display: none;*/
}
</style>
