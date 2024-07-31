<template>
  <div>
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
// JS
import axios from 'axios'
export default {
  name: 'SharkComponent',
  data() {
    return {
      msg: '',
    }
  },
  methods: {
    getResponse() {
      const path = 'http://127.0.0.1:5000/sharkcomp'
      axios
        .get(path)
        .then((res) => {
          console.log(res.data)
          this.msg = res.data
        })
        .catch((err) => {
          console.error(err)
        })
    },
  },
  created() {
    this.getResponse()
  },
}
</script>

<style>
/* CSS */
</style>
