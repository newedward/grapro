<template>
    <el-container direction="vertical">
      <manageNav  ></manageNav>
       <el-container direction="vertical">
         <template>
           <el-row type="flex"  justify="center">
             <el-button type="success" @click="checkUser">审批通过</el-button>
             <el-button type="danger" @click="delUser">审批不通过</el-button>
           </el-row>
           <el-row type="flex"  justify="center">
  <el-table
    ref="multipleTable"
    :data="tableData"
    tooltip-effect="dark"
    style="width: 60%"
    fit="False"
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      prop="type"
      label="类型"
      width="240"
    show-overflow-tooltip>
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="120">
    </el-table-column>
    <el-table-column
      prop="content"
      label="详情"
      width="360"
      show-overflow-tooltip>
    </el-table-column>
  </el-table>


    </el-row>

</template>
         </el-container>
    </el-container>
</template>

<script>
  import manageNav from '../components/manageNav'
    export default {
        name: "checkMan",
      components: {
      manageNav,
    },
      data() {
      return {
        tableData: [],
        multipleSelection: [],
        watchId:'',
      }
    },
      mounted(){
          this.getCurUserID();
      },
    methods: {
      toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            this.$refs.multipleTable.toggleRowSelection(row);
          });
        } else {
          this.$refs.multipleTable.clearSelection();
        }
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
      },
      initcheckman(){
        this.$http.post('/api/initcheckman/',{'manId':this.watchId},{emulateJSON:true})
              .then(function(response){
                 var res1 = JSON.parse(response.bodyText);
                if(res1['err_code']==0) {
                  for (var i = 0;i<res1['nlist'].length;i++){
                    this.tableData.push({
                      name:res1['nlist'][i],
                      type:'新用户注册待审批',
                      content:'注册学号为'+res1['clist'][i],
                      id:res1['ids'][i],
                    })
                  }
                    }
                    else{
                      this.$message.error("获取待审批失败")
                    }
              })
      },
      getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText);
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.initcheckman();
                  }
                })
      },
      checkUser(){
        var ids = '';
        for (var i =0;i<this.multipleSelection.length;i++){
          ids += this.multipleSelection[i].id + ',';
        }
        this.$http.post('/api/checkUser/',{'ids':ids},{emulateJSON:true})
              .then(function(response){
                 var res1 = JSON.parse(response.bodyText);
                if(res1['err_code']==0) {
                   this.$message.success("审批成功")
                  location.reload()
                  }

                    else{
                      this.$message.error("审批失败")
                    }
              })
      },
      delUser(){
        var ids = '';
        for (var i =0;i<this.multipleSelection.length;i++){
          ids += this.multipleSelection[i].id + ',';
        }
        this.$http.post('/api/delUser/',{'ids':ids},{emulateJSON:true})
              .then(function(response){
                 var res1 = JSON.parse(response.bodyText);
                if(res1['err_code']==0) {
                  this.$message.success("审批成功")
                  location.reload()

                  }

                    else{
                      this.$message.error("审批失败")
                    }
              })

      }

    }
    }
</script>

<style scoped>

</style>
