<template>
    <el-container direction="vertical">
      <manageNav  ></manageNav>
       <el-container direction="vertical">
         <el-row>
         <el-input
  placeholder="输入关键字进行过滤"
  v-model="filterText">
</el-input>

<el-tree
  class="filter-tree"
  :data="files"
  :props="defaultProps"
  @node-click="downloadnode"
  @node-contextmenu="greatpro"
  default-expand-all
  :filter-node-method="filterNode"
  ref="tree">
</el-tree>
           </el-row>
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
      mounted() {
        this.getCurUserID();
      },
      watch: {
        filterText(val) {
          this.$refs.tree.filter(val);
        }
      },
      data() {
        return {
          filterText: '',
          files: [],
          defaultProps: {
            children: 'children',
            label: 'label'
          },
          watchId: '',
        };
      },
      methods: {
        filterNode(value, data) {
          if (!value) return true;
          return data.label.indexOf(value) !== -1;
        },
        initfileman() {
          this.$http.post('/api/initFileMan/', {'manId': this.watchId}, {emulateJSON: true})
            .then(function (response) {
              var res1 = JSON.parse(response.bodyText);
              if (res1['err_code'] == 0) {
                var count = 1;
                for (var i = 0; i < res1["data"].length; i++) {
                  var item = {id: count, label: res1["data"][i][0], children: []};
                  count = count + 1;
                  for (var j = 0; j < res1["data"][i][2].length; j++) {
                    var item2 = {id: count, label: res1["data"][i][2][j][0], children: []};
                    count = count + 1;
                    for (var k = 0; k < res1["data"][i][2][j][2].length; k++) {
                      item2['children'].push({
                        id: count,
                        label: res1["data"][i][2][j][2][k][1] + res1["data"][i][2][j][2][k][3],
                        path:res1["data"][i][2][j][2][k][0],
                      })
                    }
                    item2['stu'] = res1["data"][i][2][j][1];
                    item['children'].push(item2);
                  }
                  this.files.push(item)
                }
                console.log(this.files);
              }
            })
        },
        getCurUserID() {
          this.$http.get('/api/getCurUserID')
            .then((response) => {
              var res1 = JSON.parse(response.bodyText);
              if (res1['err_num'] == 0) {
                this.watchId = res1['userID'];
                this.initfileman();
              }
            })
        },
        downloadnode(data, node, obj) {
          if (node.level === 3) {
            console.log(data.path);
          }
        },
        greatpro(event,data, node, obj){
          if (node.level === 2) {
            console.log(data.stu);
            this.$confirm('此操作将该学生毕设推举为优秀毕设并在主页展示, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'info'
        }).then(() => {
          this.$http.post('/api/makeGreatPro/',{'stuId':data.stu},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {
                      this.$message({
            type: 'success',
            message: '推举成功!'
          });
                    }
                    else{
                      this.$message.error("系统错误")
                    }

              })
        }).catch(() => {
          // this.$message({
          //   type: 'info',
          //   message: '已取消删除'
          // });
        });
          }
        }
      }
    }
</script>

<style scoped>

</style>
