<template>
    <el-container direction="vertical">
      <manageNav  ></manageNav>
       <el-container>
         <el-tree
  :props="props"
  :load="loadNode"
  lazy
  show-checkbox>
</el-tree>
         </el-container>
    </el-container>
</template>

<script>
  import manageNav from '../components/manageNav'
    export default {
        name: "fileMan",
      components: {
      manageNav,
    },
      data(){
          return {
        props: {
          label: 'name',
          children: 'zones',
          isLeaf: 'leaf'
        },
      };
      },
      methods: {
      loadNode(node, resolve) {
        if (node.level === 0) {
          return resolve([{ name: 'region' }]);
        }
        if (node.level > 1) return resolve([]);

        setTimeout(() => {
          const data = [{
            name: 'leaf',
            leaf: true
          }, {
            name: 'zone'
          }];

          resolve(data);
        }, 500);
      }
    }
    }
</script>

<style scoped>

</style>
