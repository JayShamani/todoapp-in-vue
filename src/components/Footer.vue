<template>
  <div class="footer">
    <div class="footerelements">
      <div>Created by: Jay Shamnani</div>
      <div>
        Github:
        <a href="https://github.com/JayShamani"
          >https://github.com/JayShamani</a
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
.footer {
  position: fixed;
  padding: 5px;
  bottom: 0%;
  width: 100%;
  background-color: #121212;
  color: #ffffff;
  font-size: auto;
}

.footerelements {
  display: flex;
  justify-content: space-around;
}
</style>
