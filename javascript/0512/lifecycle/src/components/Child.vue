<template>
  <div>
    <span ref="childText">{{ childText }}</span>
  </div>
</template>

<script>
export default {
  name: 'Child',
  data() {
    return {
      childText: '응애'
    }
  },
  created() {
    console.log('------ Child.vue Created ------')
  },
  mounted() {
    console.log('------ Child.vue Mounted ------')
  },
  destroyed() {
    console.log('------ Child.vue Destroyed ------')
    console.log(this.$refs['childText'])
    // this.$emit('child-destroyed', this.childText)
  }
}
</script>

<style>

</style>