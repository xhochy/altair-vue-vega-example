<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout column align-center>
        <v-btn @click.native="reloadImage()">Reload</v-btn>
        <div id="vega-box"></div>
      </v-layout>
    </v-slide-y-transition>
  </v-container>
</template>

<script>
import {default as vegaEmbed} from 'vega-embed'

export default {
  methods: {
    reloadImage () {
      fetch('/vega-example').then(response => {
        response.json().then(spec => {
          vegaEmbed('#vega-box', spec, {actions: false})
        })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
