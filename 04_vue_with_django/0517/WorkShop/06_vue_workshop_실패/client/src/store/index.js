import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [],
    isLogin: false,
    token: '',
  },
  getters: {
    config: function (state) {
      return `JWT ${state.token}`
    }
  },
  mutations: {
    SET_TODOS: function (state, todos) {
      state.todos = todos
    },
    DELETE_TODO: function (state, todoId) {
      state.todos = state.todos.filter(todo => {
        if (todo.id !== todoId) {
          return todo
        }
      })
    },
    UPDATE_TODO_STATUS: function (state, updatedTodo) {
      state.todos = state.todos.map(todo => {
        if (todo.id === updatedTodo.id) {
          return { ...updatedTodo }
        } else { 
          return { ...todo }
        }
      })
    },
    LOGIN: function (state, token) {
      state.isLogin = true
      state.token = token
    },
    LOGOUT: function (state) {
      state.isLogin = false
      state.token = null
    },
  },
  actions: {
    getTodosFromServer: function ({ commit }, config) {
      console.log(config)
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
        headers: config,
      })
        .then((res) => {
          commit('SET_TODOS', res.data)
        })
        .catch(err => console.log(err))
    },
    createTodo: function (context, title, config) {  
      if (title) {
        const todoItem = { title: title, }
        console.log(config)
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: todoItem,
          headers: config,
        })
          .then(function () {
            router.push({ name: 'TodoList' }) 
          })
          .catch(err => console.log(err))
        }
    },
    deleteTodo: function ({ commit }, todo) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`
      })
        .then(res => {
          commit('DELETE_TODO', res.data.id)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function ({ commit }, todo) {
      const todoItem = {
        ...todo,
        completed: !todo.completed
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
      })
        .then((res) => {
          commit('UPDATE_TODO_STATUS', res.data)
        })
        .catch(err => console.log(err))
    },
    signup: function (context, credential) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: credential,
      })
        .then(function () {
          router.push({ name: 'Login' })
        })
        .catch(err => console.log(err))
    },
    login: function ({ commit }, credential) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: credential,
      })
        .then(res => {
          const token = res.data.token
          localStorage.setItem('jwt', token)
          commit('LOGIN', token)
          router.push({name: 'TodoList' })
        })
        .catch(err => console.log(err))
    },
    logout: function ({ commit }) {
      localStorage.removeItem('jwt')
      commit('LOGOUT')
    }
  },
  modules: {
  }
})
