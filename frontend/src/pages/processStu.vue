<template>
  <div id = "process">

    <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container>
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowStu  ></flowStu>
      </el-aside>
        <el-main>
          <div class="block">
  <el-timeline >
    <el-timeline-item timestamp="2020/10/12" placement="top">
      <el-card>
        <h4>题目选择</h4>
        <p>朱振南 选择题目 毕业设计管理系统</p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2020/11/25" placement="top">
      <el-card>
        <h4>开题</h4>
        <p>朱振南 完成开题报告 </p>
      </el-card>
    </el-timeline-item>
    <el-timeline-item timestamp="2020/12/2" placement="top">
      <el-card>
        <h4>开题报告修正</h4>
        <p>何清刚 老师 提出修改意见</p>
      </el-card>
    </el-timeline-item>
  </el-timeline>
             </div>


        </el-main>
      </el-container>
    </el-container>
</div>
</template>

<style>

  .el-row {
    margin-bottom: 20px;
    border-radius: 4px;
  }
  .el-roe-title{
    margin-bottom: 20px;

  }
  .el-col {
    border-radius: 4px;
  }
  .el-header-home{
    line-height: 40px;
    font-size: 20px;
  }
  .blog{
    background: #EEE ;
    border-radius: 10px;
    margin-bottom: 20px;
  }
  .infinite-list-wrapper{
    height: 100vh;
  }
  .el-table .warning-row {
    background: oldlace;
  }
  #stu{
    margin:8px 10px;
  }

  .el-table .success-row {
    background: #f97880;
  }
</style>

<script>
import topNav from '../components/topNav'
import flowTea from '../components/flowTea'
import flowStu from '../components/flowStu'
  export default {
    name: 'home',
    components: {
      topNav,
      flowStu,
    },
    mounted() {
          this.getCurUserID();
      },
    methods: {
      tableRowClassName({row, rowIndex}) {
        if (rowIndex === 1) {
          return 'warning-row';
        } else if (rowIndex === 2) {
          return 'success-row';
        }
        return '';
      },
      getCurUserID(){
        this.$http.get('/api/getCurUserID')
                .then((response) => {
                  var res1 = JSON.parse(response.bodyText)
                  if (res1['err_num'] == 0) {
                    this.watchId = res1['userID'];
                    this.role = res1['role'];
                    this.getdata();
                  }
                  else{
                      this.$message.error("系统错误")
                    }
                })
      }
    },
    data() {
      return {
        tableData: [{
          number: '171110133',
          name: '朱振南',
          status: '选择题目 毕业设计全流程管理系统',
        }, {
          number: '171110114',
          name: '航子',
          status: '完成题目'
        }, {
          number: '182210922',
          name: '王小虎',
          status: '选择题目',
        }, {
          number: '198764522',
          name: '王小虎',
          status: '结题'
        }],
        watchId:'',
        role:''
      }
    }
  }
</script>
