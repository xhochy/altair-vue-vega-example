Example web app that display data using Altair, Vega and VueJS
==============================================================

This is demo I used at PyData Amsterdam 2018.

Setup
-----

To reproduce the content of this demo, you will need a working Python and
Node.JS setup. Also, you will need to have [Vue](https://vuejs.org/) installed
in your global Node installation:

```
npm install -g vue-cli
```

Then you can use `vue` to instantiate a new application template. We use the
more complicated webpack example here as we want to have a running webpack
server.

```
vue init vuetifyjs/webpack altair-app
```

 * In `build/webpack.dev.conf.js`, we have added `disableHostCheck: true` so that
   in development the server is accesible from any hosts. This allows port
   forwarding to other hosts, e.g. when running from a container.
 * In `src/App.vue`, we have switched the the headings to highlight that this is
   used in a tutorial at PyData Amsterdam.
 * In `config/index.js` add an entry that will forward to our local Flask app
   where we will generate the Vega spec using Altair.
   ```
   proxyTable: {
     '/vega-example': 'http://localhost:5000'
   },
   ```
 * Install `vega-embed` using npm install --save vega-embed
 * In `HelloWorld.vue`, we have added a script section that will call our Flask
   backend that returns the Vega specification using Altair.

Run the `javascript` part using `npm run dev` and the Flask backend using
`FLASK_APP=app.py flask run`.
