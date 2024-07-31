<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- html code -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lumen/bootstrap.min.css"
        integrity="sha384-GzaBcW6yPIfhF+6VpKMjxbTx6tvR/yRd/yJub90CqoIn2Tz4rRXlSpTFYMKHCifX"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Games Library 🎲
          </h1>
          <hr />
          <br />

          <b-alert varaint="warning" v-if="showMessage" show>{{
            alert_msg
          }}</b-alert>

          <button class="btn btn-success" type="button" v-b-modal.game-modal>
            Add game
          </button>
          <br /><br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Played ?</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(game, index) in games" :key="index">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>
                  <span v-if="game.played">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      class="btn btn-info btn-sm"
                      v-b-modal.game-update-modal
                      @click="editGame(game)"
                    >
                      Update
                    </button>
                    <button
                      class="btn btn-danger btn-sm"
                      @click="deleteGame(game)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="text-center bg-primary text-white"
            style="border-radius: 5px"
          >
            Project by Tanush Tambe
          </footer>
        </div>
      </div>
      <!-- START OF ADD GAME MODAL -->
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add a new game"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addGameForm.title"
              required
              placeholder="Enter Games:"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-genre-group"
            label="Genre:"
            for="form-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              v-model="addGameForm.genre"
              required
              placeholder="Enter Genre:"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-played-group">
            <b-form-checkbox-group v-model="addGameForm.played" id="form-check">
              <b-form-checkbox value="true">Played ?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-modal>

      <!-- END OF ADD GAME MODAL -->

      <!-- START OF UPDATE MODAL -->
      <b-modal
        ref="editGameModal"
        id="game-update-modal"
        title="Update a game"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onUpdateSubmit" @reset="onUpdateReset" class="w-100">
          <b-form-group
            id="update-form-title-group"
            label="Title:"
            for="update-form-title-input"
          >
            <b-form-input
              id="update-form-title-input"
              type="text"
              v-model="updateForm.title"
              required
              placeholder="Enter Game:"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="update-form-genre-group"
            label="Genre:"
            for="update-form-genre-input"
          >
            <b-form-input
              id="update-form-genre-input"
              type="text"
              v-model="updateForm.genre"
              required
              placeholder="Enter Genre:"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group id="update-form-played-group">
            <b-form-checkbox-group v-model="updateForm.played" id="form-check">
              <b-form-checkbox value="true">Played ?</b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>

          <b-button type="submit" variant="info">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-form>
      </b-modal>

      <!-- END OF UPDATE MODAL -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'GamesComponent',
  data() {
    return {
      games: [],
      addGameForm: {
        title: '',
        genre: '',
        played: false,
      },
      updateForm: {
        id: '',
        title: '',
        genre: '',
        played: false,
      },
      showMessage: false,
      alert_msg: '',
    }
  },
  methods: {
    getGames() {
      const path = 'http://127.0.0.1:5000/api/games'
      axios
        .get(path)
        .then((res) => {
          if (res.data.status == 'success') {
            this.games = res.data.games
          } else if (res.data.status == 'failure') {
            this.alert_msg = 'Something went wrong !'
          }
        })
        .catch((err) => {
          this.alert_msg = 'Something went wrong !'
          console.error(err)
        })
    },
    addGame(payload) {
      const path = 'http://127.0.0.1:5000/api/games'
      axios
        .post(path, payload)
        .then(() => {
          this.getGames()
          this.alert_msg = 'Game added successfully !'
          this.showMessage = true
        })
        .catch((err) => {
          console.error(err)
        })
      this.getGames()
    },
    initForm() {
      this.addGameForm.title = ''
      this.addGameForm.genre = ''
      this.addGameForm.played = []
      this.updateForm.id = ''
      this.updateForm.title = ''
      this.updateForm.genre = ''
      this.updateForm.plare = []
    },
    onSubmit(e) {
      e.preventDefault()
      this.$refs.addGameModal.hide()
      let played = false
      if (this.addGameForm.played[0]) {
        played = true
      }
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        played: played,
      }
      this.addGame(payload)
      this.initForm()
    },
    onReset(e) {
      e.preventDefault()
      this.$refs.addGameModal.hide()
      this.initForm()
      this.getGames()
    },
    updateGame(id) {
      const path = `http://127.0.0.1:5000/api/games`
      axios
        .put(path, {
          id: id,
          title: this.updateForm.title,
          genre: this.updateForm.genre,
          // played: this.updateForm.played,
        })
        .then(() => {
          this.getGames()
          this.alert_msg = 'Game updated !'
          this.showMessage = true
        })
        .catch((err) => {
          console.error(err)
          this.showMessage = 'Error !'
        })
      this.getGames()
    },
    editGame(game) {
      this.updateForm = game
    },
    onUpdateSubmit(e) {
      e.preventDefault()
      this.$refs.editGameModal.hide()
      let played = false
      if (this.updateForm.played[0]) {
        played = true
      }
      const payload = {
        title: this.updateForm.title,
        genre: this.updateForm.genre,
        played: played,
      }
      this.updateGame(payload, this.updateForm.id)
      this.initForm()
    },

    onUpdateReset(e) {
      e.preventDefault()
      this.$refs.editGameModal.hide()
      this.initForm()
      this.getGames()
    },
    removeGame(id) {
      const path = `http://127.0.0.1:5000/game/${id}`
      axios
        .delete(path)
        .then(() => {
          this.getGames()
          this.alert_msg = 'Game deleted !'
          this.showMessage = true
        })
        .catch((err) => {
          console.error(err)
          this.showMessage = 'Error !'
          this.showMessage = true
        })
      this.getGames()
    },
    deleteGame(game) {
      this.removeGame(game.id)
    },
  },

  created() {
    this.getGames()
  },
}
</script>

<style>
/* CSS */
</style>
