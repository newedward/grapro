<template>
  <div id = "processTea">

    <el-container height= "100%" direction="vertical">
      <topNav></topNav>
      <el-container>
        <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <flowTea  ></flowTea>
      </el-aside>
        <el-main>
          <div id="stu" >
<div id="block">
    <span class="demonstration">开题提交截止日期</span>
              <el-divider direction="vertical"></el-divider>
    <el-date-picker
      v-model="value1"
      type="datetime"
      placeholder="选择日期时间"
      align="right"
      :picker-options="pickerOptions">
    </el-date-picker>
</div>

<div id="block">
    <span class="demonstration">中期提交截止日期</span>
              <el-divider direction="vertical"></el-divider>
    <el-date-picker
      v-model="value2"
      type="datetime"
      placeholder="选择日期时间"
      align="right"
      :picker-options="pickerOptions">
    </el-date-picker>

</div>
            <div id="block">
    <span class="demonstration">结题提交截止日期</span>
              <el-divider direction="vertical"></el-divider>
    <el-date-picker
      v-model="value3"
      type="datetime"
      placeholder="选择日期时间"
      align="right"
      :picker-options="pickerOptions">
    </el-date-picker>
</div>
            <el-divider><i class="el-icon-s-data"></i></el-divider>
    <el-table id="table"
    :data="tableData"
    style="width: 100%"
    :row-class-name="tableRowClassName">
    <el-table-column
      prop="number"
      label="学号"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="status"
      label="状态">
    </el-table-column>
  </el-table>
  </div>

        </el-main>
      </el-container>
    </el-container>
</div>
</template>

<style>

  #block{
    margin: 2% 10px;
  }
  #table{
    box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
    margin-top: 2%;
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
  export default {
    name: 'home',
    components: {
      topNav,
      flowTea,
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
      },
      getdata(){
        this.$http.post('/api/getTeacherProcess/',{'userId':this.watchId},{emulateJSON:true})
              .then(function(response){
                    var res1 = JSON.parse(response.bodyText);
                    if(res1['err_code']==0) {

                    }
                    else{
                      this.$message.error("获取流程信息失败")
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
        role:'',
        pickerOptions: {
          shortcuts: [{
            text: '今天',
            onClick(picker) {
              picker.$emit('pick', new Date());
            }
          }, {
            text: '明天',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() + 3600 * 1000 * 24);
              picker.$emit('pick', date);
            }
          }, {
            text: '一周后',
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() + 3600 * 1000 * 24 * 7);
              picker.$emit('pick', date);
            }
          }]
        },
        value1: '',
        value2: '',
        value3:'',
      }
    }
  }
</script>
