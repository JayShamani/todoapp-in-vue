<template>
  <div class="addTaskContainer">
    <div class="addTask">
      <form @submit="onSubmit" class="addForm">
        <div class="col-sm-12">
          <label class="col-4">Heading</label>
          <input class="col-7" type="text" v-model="head" name="head" />
        </div>
        <div class="col-sm-12">
          <label class="col-4">Task</label>
          <input class="col-7" type="text" v-model="body" name="body" />
        </div>
        <div class="col-sm-12">
          <label class="col-4">Reminder</label>
          <input type="checkbox" v-model="reminder" name="reminder" />
        </div>
        <div class="addtaskBtn">
          <button type="submit" class="btn btn-success">Add Task</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "addTask",
  data() {
    return {
      head: "",
      body: "",
      reminder: false,
    };
  },
  computed: mapGetters(["Profilestore"]),
  methods: {
    ...mapActions(["addTask"]),
    onSubmit(e) {
      e.preventDefault();

      if (this.Profilestore.Profile !== 0) {
        if (!this.head) {
          alert("Please Enter Heading for Task");
        } else {
          const newTask = {
            taskhead: this.head,
            taskbody: this.body,
            taskreminder: this.reminder,
            taskauthor: this.Profilestore.Profile,
          };
          this.$emit("addTask", newTask);
          this.addTask(newTask);
          this.head = "";
          this.body = "";
          this.reminder = false;
        }
      } else {
        alert("Please Login to add a task");
      }
    },
  },
};
</script>

<style scoped>
.addTaskContainer {
  padding-bottom: 50px;
  display: flex;
  justify-content: space-around;
  color: #fff;
  transition: 0.3s ease;
  transform: inherit;
}
.addTask {
  width: 80%;
  background: #121212;
  border-radius: 10px;
  padding-top: 5px;
}

.addtaskBtn {
  display: flex;
  width: 100%;
  padding: 5px;
  justify-content: center;
}

.addForm {
  width: 100%;
  display: block;
  padding: 5px;
}
form label {
  text-align: right;
}
form input {
  border: none;
  background-color: #3c403c;
  border-radius: 5px;
  color: #fff;
}
</style>
