<template>
  <div id="app">
    <span ref="appNumber">{{ number }}</span>
    <button @click="increase">++</button>
    <hr>
    <span ref="appText">{{ text }}</span>
    <hr>
    <button @click="activeToggle">toggle</button>
    <Child v-if="isActive" />
  </div>
</template>

<script>
import Child from './components/Child'

export default {
  name: 'App',
  components: {
    Child
  },
  data() {
    return {
      text: '',
      number: 0,
      isActive: true,
    }
  },
  beforeCreate() {
    console.log('------ App.vue beforeCreate ------')
    console.log(this.text)
    this.text = 'App.vue는 아직 create 되지 않았습니다.'
    console.log(this.text)
  },
  created() {
    console.log('------ App.vue is Created ------')
    // console.log(this.$el)
    this.text = 'App.vue가 create 되었습니다!!'
    console.log(this.text)
    console.log(this.$refs['appText'])
    this.increase()
  },
  beforeMount() {
    console.log('------ App.vue beforeMount ------')
    console.log(this.text)
    console.log(this.$refs['appText'])
  },
  mounted() {
    console.log('------ App.vue is Mounted ------')
    // console.log(this.$el)
    // console.log(this.$refs['appText'])
    // this.text = 'App.vue가 mount 되었습니다!!'
    console.log(this.$refs['appText'])
  },
  beforeUpdate() {
    console.log('------ App.vue is beforeUpdate ------')
    // console.log(this.number)
    // console.log(this.$refs['appNumber'])
  },
  updated() {
    console.log('------ App.vue is Updated ------')
    // console.log(this.number)
    // console.log(this.$refs['appNumber'])
  },
  methods: {
    increase() {
      this.number++
    },
    activeToggle() {
      this.isActive = !this.isActive
    }
  },
  watch: {
    number: function (newval, old) {
      console.log(newval, old)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
