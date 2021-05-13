import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoList: [],
  },
  getters: {
    getTodoList: function (state) {
      return state.todoList
    },
  },
  mutations: {
    ADD_TODO: function (state, todoItem) {
      state.todoList.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      const idx = state.todoList.indexOf(todoItem)
      state.todoList.splice(idx, 1)
    },
    UPDATE_TODO(state, todoItem) {
      const idx = state.todoList.indexOf(todoItem)
      state.todoList[idx].completed = !state.todoList[idx].completed
    },
  },
  actions: {
    addTodo: function ({ commit }, title) {
      const todoItem = {
        title,
        completed: false,
      }
      commit('ADD_TODO', todoItem)
    },
    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },
    updateTodo({ commit }, todoItem) {
      commit('UPDATE_TODO', todoItem)
    },
  },
  modules: {
  }
})
